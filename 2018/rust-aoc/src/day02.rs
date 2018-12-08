#![feature(test)]

extern crate test;

use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;

fn part1(input: &str) -> i32 {
    let mut two_count = 0;
    let mut three_count = 0;
    input
        .lines()
        .for_each(|n| {
            let mut letters = HashMap::new();
            for c in n.chars() {
                *letters.entry(c).or_insert(0) += 1;
            }
            if letters.values().any(|&x| x == 3) {
                three_count += 1;
            }

            if letters.values().any(|&x| x == 2) {
                two_count += 1;
            }
        });
    return three_count*two_count
}

fn part2(input: &str) -> String {
    for (idx, id) in input.lines().enumerate() {
        for id2 in input.lines().skip(idx + 1) {
            if id.chars().zip(id2.chars()).filter(|(a,b)| a!=b).count() == 1 {
                return id
                        .chars()
                        .zip(id2.chars())
                        .filter(|(a,b)| a==b)
                        .map(|(a,_)| a)
                        .collect();
            }
        }
    }
    unreachable!()
}

fn main() {
    let mut contents = String::new();
    File::open("../data/input02.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong reading the file");

    println!("Part 1: {}", part1(&contents));
    println!("Part 2: {}", part2(&contents));
}

#[cfg(test)]
mod tests {
    use super::*;
    use test::{Bencher, black_box};

    #[test]
    fn test_p1(){
        assert_eq!(part1("abcdef\nbababc\nabbcde\nabcccd\naabcdd\nababab\nabcdee"), 12);
    }

    #[test]
    fn test_p2(){
        assert_eq!(part2("abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz"), "fgij");
    }

    #[bench]
    fn bench_part1(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/input02.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");

        b.iter(|| {
            part1(&contents);
        });
    }

    #[bench]
    fn bench_part2(b: &mut Bencher) {
        let mut contents = String::new();
        File::open("../data/input02.txt")
            .expect("File not found")
            .read_to_string(&mut contents)
            .expect("Something went wrong reading the file");

        b.iter(|| {
            part2(&contents);
        });
    }
}
