from pwn import *

import gzip

import binaryninja

r = remote('07u4-1.play.hfsc.tf', 3991)

r.sendlineafter(b'Play', b'2')

for bin_num in range(25):
    print('solving bin', bin_num)
    r.recvuntil(b'BIN')

    r.recvline()
    binary = r.recvline()

    filename = f'bins/bin{bin_num}'

    with open(filename, 'wb') as f:
        f.write(gzip.decompress(unhex(binary)))

    with binaryninja.load(filename) as bv:
        func = bv.get_functions_by_name('main')[0]
        lfunc = func.llil
        func = func.hlil

        answer = ''

        if len(func.basic_blocks) == 11:
            print("type 1")
            val = []
            for bb in func.basic_blocks:
                ins = bb[0]
                assert isinstance(ins, binaryninja.HighLevelILInstruction)
                if ins.operation == binaryninja.HighLevelILOperation.HLIL_IF:
                    def is_xor(ins: binaryninja.HighLevelILInstruction):
                        if isinstance(ins, binaryninja.HighLevelILXor):
                            if isinstance(ins.operands[-1], binaryninja.HighLevelILConst):
                                return ins.operands[-1].value.value
                    xor_const = next(ins.traverse(is_xor))
                if ins.operation != binaryninja.HighLevelILOperation.HLIL_VAR_INIT:
                    continue
                if ins.operands[1].operands[0].var.name != 'argv':
                    continue
                inss = bb[4:-1]
                assert isinstance(inss, list)
            for i in inss:
                assert i.operation == binaryninja.HighLevelILOperation.HLIL_VAR_INIT
                val.append(i.operands[-1].value.value)

            for i in val:
                answer += chr(i ^ xor_const)
        elif len(func.basic_blocks) == 12:
            print("type 2")
            val = []
            for bb in func.basic_blocks:
                ins = bb[0]
                assert isinstance(ins, binaryninja.HighLevelILInstruction)
                if ins.operation == binaryninja.HighLevelILOperation.HLIL_IF:
                    def is_xor(ins: binaryninja.HighLevelILInstruction):
                        if isinstance(ins, binaryninja.HighLevelILXor):
                            if isinstance(ins.operands[-1], binaryninja.HighLevelILConst):
                                return ins.operands[-1].value.value
                    xor_const = next(ins.traverse(is_xor))

            for i in lfunc.basic_blocks[3][1:-2]:
                assert i.operation == binaryninja.LowLevelILOperation.LLIL_STORE
                val.append(i.operands[-1].value.value)

            print(val)
            for i in val:
                answer += chr(i ^ xor_const)
            print('answer', answer)
        elif len(func.basic_blocks) == 16:
            print("type 3")

            input_len = func.basic_blocks[2][0].operands[-1].operands[-1][0].value.value

            big_bb = func.basic_blocks[7]
            assert not isinstance(big_bb, list)
            val = []
            for i in big_bb[2:2+(input_len//2)]:
                val.append(i.operands[-1].value.value)
            comp = []
            for i in big_bb[2+(input_len//2):-1]: # was 48:-1
                comp.append(i.operands[-1].value.value)

            ans = []
            for i,j in zip(val, comp):
                ans.append(chr(((j-i)>>8)%256))
                ans.append(chr((j-i)%256))

            answer = ''.join(ans)
        elif len(func.basic_blocks) == 6:
            print("type 4")
            answer = func.basic_blocks[2][-2].operands[-1][1].string[0]
        elif len(func.basic_blocks) == 8 and len(func.basic_blocks[0]) > 4:
            print("type 5")

            input_len = func.basic_blocks[0][2].operands[-1].operands[-1][0].value.value

            big_bb = func.basic_blocks[0]
            assert not isinstance(big_bb, list)
            val = []
            for i in big_bb[7:7+(input_len//2)]:
                val.append(i.operands[-1].value.value)
            comp = []
            for i in big_bb[7+(input_len//2):-1]:
                comp.append(i.operands[-1].value.value)

            ans = []
            for i,j in zip(val, comp):
                ans.append(chr(((j-i)>>8)%256))
                ans.append(chr((j-i)%256))

            answer = ''.join(ans)
        elif len(func.basic_blocks) == 8 and len(func.basic_blocks[0]) == 4:
            print("type 6")
            answer = func.basic_blocks[2][-2].operands[-1][1].string[0]
        elif len(func.basic_blocks) == 5 and len(func.basic_blocks[0]) == 9:
            print("type 7")
            answer = func.basic_blocks[0][-3].operands[-1][1].string[0]
        elif len(func.basic_blocks) == 15:
            print("type 8")
            val = []
            for bb in func.basic_blocks:
                ins = bb[0]
                assert isinstance(ins, binaryninja.HighLevelILInstruction)
                if ins.operation == binaryninja.HighLevelILOperation.HLIL_IF:
                    def is_xor(ins: binaryninja.HighLevelILInstruction):
                        if isinstance(ins, binaryninja.HighLevelILXor):
                            if isinstance(ins.operands[-1], binaryninja.HighLevelILConst):
                                return ins.operands[-1].value.value
                    xor_const = next(ins.traverse(is_xor))

            for i in func.basic_blocks[6][1:-1]:
                assert i.operation == binaryninja.HighLevelILOperation.HLIL_VAR_INIT
                val.append(i.operands[-1].value.value)

            for i in val:
                answer += chr(i ^ xor_const)
        else:
            print('unknown binary type!')
            exit(0)

    print(answer)
    r.sendline(answer.encode('charmap'))

r.interactive()

# midnight{Ti_esrever_dna_ti_pilf_nwod_gnaht_ym_tup_i}
