//#![feature(test)]

//extern crate test;

use std::fs::File;
use std::io::prelude::*;
use std::collections::HashSet;

type NumType = i32;

fn check_row_hor(board: &Vec<NumType>, seen: &HashSet<NumType>) -> bool {
    (0..5)
        .any(|i| board[i*5..(i*5)+4]
            .iter()
            .all(|a| seen.contains(a))
        )
}

fn check_row_vert(board: &Vec<NumType>, seen: &HashSet<NumType>) -> bool {
    (0..5)
        .any(|i| seen.contains(&board[i]) && seen.contains(&board[i+5]) && seen.contains(&board[i+10]) &&
            seen.contains(&board[i+15]) && seen.contains(&board[i+20])
        )
}

fn play_board(numbers: &Vec<NumType>, board: &Vec<NumType>) -> (usize, NumType) {
    let mut seen: HashSet<NumType> = HashSet::new();
    
    for (idx, bingo_number) in numbers.iter().enumerate() {
        seen.insert(*bingo_number);

        if check_row_hor(&board, &seen) || check_row_vert(&board, &seen) {
            let remaining_sum: NumType = board.iter().filter(|b| !seen.contains(b)).sum();
            return (idx, *bingo_number*remaining_sum)
        }
    }

    (0,0)
}

fn main(){
    let mut contents = String::new();
    File::open("../data/04.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");

    let mut lines = contents
        .split("\n\n");
    
    let numbers = lines.next()
        .map(|n| n.split(",").map(|s| s.parse::<NumType>().unwrap()))
        .unwrap()
        .collect::<Vec<NumType>>();

    let boards = lines
        .map(|board| board
            .split("\n")
            .flat_map(|line|
                line
                .split_whitespace()
                .map(|n| n.parse::<NumType>().unwrap())
            )
            .collect::<Vec<NumType>>()
        )
        .collect::<Vec<Vec<NumType>>>();

    let finished_boards = boards
        .iter()
        .map(|b| play_board(&numbers, b))
        .filter(|(idx, _score)| *idx != 0)
        .collect::<Vec<(usize, NumType)>>();

    let part_1 = finished_boards
        .iter()
        .min_by(|x,y| x.0.cmp(&y.0))
        .unwrap()
        .1;
    let part_2 = finished_boards
        .iter()    
        .max_by(|x,y| x.0.cmp(&y.0))
        .unwrap()
        .1;

    println!("Part 1 {}", part_1);  
    println!("Part 2 {}", part_2);
}
