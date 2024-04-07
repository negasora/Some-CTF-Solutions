use hex_literal::hex;
use itertools::Itertools;
use rayon::prelude::*;


use md5::{Digest, Md5};


fn main() {
    let ctxt: [u8; 104] = [94, 13, 26, 2, 24, 90, 111, 95, 11, 10, 18, 28, 90, 104, 12, 8, 79, 61, 68, 13, 2, 31, 0, 86, 19, 1, 11, 9, 11, 11, 84, 9, 28, 67, 5, 10, 25, 14, 72, 104, 89, 12, 29, 74, 110, 49, 11, 12, 69, 16, 9, 5, 5, 95, 78, 61, 39, 31, 35, 83, 27, 2, 69, 82, 59, 22, 13, 93, 48, 7, 12, 85, 20, 92, 58, 70, 3, 59, 14, 85, 24, 92, 9, 110, 89, 1, 27, 91, 124, 89, 75, 0, 10, 10, 22, 74, 110, 89, 76, 1, 17, 27, 9, 90];

    let mut hasher = Md5::new();
    let expected = hex!("a8379015e5a77cfe783b87b3058672f3").into();
    //let expected = [4, 134, 183, 104, 79, 22, 255, 245, 238, 34, 13, 8, 201, 134, 106, 204];

    hasher.update(&ctxt);

    println!("{:?}", hasher.finalize_reset());

    let mut ptxt: [u8; 104] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

    let mut last = 0;

    let key_len = 5;

    for key in (0..key_len).map(|_| 65..0x7a).multi_cartesian_product() {
        for (i, c) in ctxt.iter().enumerate() {
            ptxt[i] = key[i%key_len] ^ c;
        }
        hasher.update(&ptxt);
        if hasher.finalize_reset() == expected
        {
            println!("{:?}", &key);
            return;
        }
        if key[0] != last
        {
            last = key[0];
            println!("{}", last);
        }
    }
}
