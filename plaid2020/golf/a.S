;build:
; nasm -f bin a.S -o a.so
;
;test:
; LD_PRELOAD=./a.so /bin/true
;
;debug:
; gdb sh
; r -c 'LD_PRELOAD=./a.so /bin/true'

bits 64
org    0x00000000      ;Program load offset

ehdr:
    ; e_ident
    db 0x7F, "ELF" ;ei_mag
    db 2 ; ei_class
    db 1 ; ei_data
    db 1 ; ei_version
    db 0 ; ei_osabi
    db 0 ; ei_abiversion
    
    times 7 db 0 ; zero padding
    
    dw 3 ; e_type
    dw 0x3e ; e_machine
    dd 1 ; e_version
    binsh:
    dq "/bin/sh";0x68732f6e69622f ; e_entry (this program enters at /bin/sh)
    dq phdr            ; e_phoff
beginning:
    ;dq 0 ;e_shoff
    ;dd 0 ;e_flags
    ; 12 bytes, needs to end in jump to loc1
    sub al, $ - binsh ; 2, loads binsh into rax
    mov rdi, rax ; 3
    sub al, 0x8 ; 2
    mov [rax], r8; 3, r8 is 0
    sub al, 0x8 ; 2
    jmp loc1 ; 2
    ;dw 0 ;e_ehsize can be used for storage too!
    dw 0x38             ;e_phentsize:  program header size (0x38)
    dw 2                    ;e_phnum:      two program headers
phdr:
    dd 1                    ;overlap e_shentsize and p_type
    dd 7                    ;overlap e_shnum and p_flags

    dq 0                    ;p_offset (first half also e_shstrndx)
    dq $$                   ;p_vaddr:      start of the current section
loc1:
    ;dq 0x1000 ;p_paddr
    mov [rax], rdi ; 3
    xchg rsi, rax ; 2
    xchg r8, rax ; 2
    push rax ; 1

;dq 0 ; p_filesz
    pop rdx ; 1
    mov al, 0x3b ; 2
    syscall ; 2
    nop ; 1
    nop ; 1
    nop ; 1
    dq 6 ; p_memsz needs to be 0 for p_memsz restrictions
    dq 0x1000 ; p_align
    
    dd 2 ;p_type dynamic
    dd 7 ;p_flags rwx
    dq dynsec - $$ ;p_offset
    dq dynsec ;p_vaddr
    ;dq 0x4141414141414141 ;p_paddr

_start:
dynsec:
; DT_INIT overlaps
    dq 12 ; p_memsz
    dq beginning ;p_align

; DT_SYMTAB
dq 6
dq 0x41414141
; DT_STRTAB
db 5
; reads DT_STRTAB and DT_NULL off end
