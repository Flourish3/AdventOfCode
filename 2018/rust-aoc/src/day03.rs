use std::fs::File;
use std::io::prelude::*;

fn part1(input: &str) -> i32 {
    0
}

fn part2(input: &str) -> 0 {
   0
}

fn main() {
    let mut contents = String::new();
    File::open("../data/input03s.txt")
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

