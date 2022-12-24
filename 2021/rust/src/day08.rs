//#![feature(test)]

//extern crate test;

use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;
use itertools::Itertools;


fn main() {
    let mut contents = String::new();
    File::open("../data/08.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");
    let initial: Vec<(Vec<&str>, Vec<&str>)> = contents
        .lines()
        .map(|l| l.split_once(" | ")
            .map(|(input,output)| 
                (input.split(" ").collect::<Vec<&str>>(), output.split(" ").collect::<Vec<&str>>()))
            .unwrap()
        )
        .collect();

        println!("intitial {:?}", initial);

        let first_count = initial
            .iter()
            .map(|(i,o)| {let a = o
                .iter()
                .filter(|sub_o| {
                    let sub_count = (***sub_o).chars().count();
                    println!("sub count of {} is {}", sub_o, sub_count);
                    sub_count == 2 || sub_count == 3 || 
                    sub_count == 4 || sub_count == 7 
            })
            .collect::<Vec<&&str>>();
                println!("{:?}", a);
                a.len()
            }
            ).collect::<Vec<usize>>();
            println!("{:?}", first_count);

            let b : usize= first_count.iter().sum();

        println!("Part 1 {}", b);
}

#[cfg(test)]
mod tests {
    use super::*;


}
