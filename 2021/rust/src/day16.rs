//#![feature(test)]

//extern crate test;

use std::fs::File;
use std::io::prelude::*;



#[derive(PartialEq, Debug)]
struct Packet {
    version: u32,
    type_id: u32,
    length_bit: Option<u32>,
    length: Option<u32>,
    literal: Option<u32>,
    sub_packets: Option<Vec<Packet>>
}

fn parse_literal(block: &[u8]) -> u32 {
    let tails: Vec<u8> = block
        .chunks(5)
        .flat_map(|c| c.to_vec().iter().skip(1).map(|o| (*o)).collect::<Vec<u8>>())
        .collect();
    
    to_binary(tails)
}

fn to_binary(block: Vec<u8>) -> u32 {
    block
        .iter()
        .rev()
        .enumerate()
        .fold(0_u32, |acc,(idx, bin)| acc + (*bin as u32)*2_u32.pow(idx as u32))
}

fn parse_sub_packs(blocks: Vec<u8>) -> Vec<Packet> {

}

fn parse_block(block_bits: Vec<u8>) -> Packet {
    let version = to_binary(block_bits[0..3].to_vec());
    let type_id = to_binary(block_bits[3..6].to_vec());

    //print!("{}, {}", version, type_id);

    if type_id == 4 {

        let end_diff = (block_bits.len() - 6)  % 5;

        let literal = parse_literal(&block_bits[6..block_bits.len() - end_diff]);

        Packet{
            version: version,
            type_id: type_id,
            length_bit: None,
            length: None,
            literal: Some(literal),
            sub_packets: None,
        }
    } else {
        let length = if block_bits[7] == 0 {
            to_binary(block_bits[8..23].to_vec())
        } else {
            to_binary(block_bits[8..19].to_vec())
        };
        let start = if block_bits[7] == 0 {23} else {19};
        let sub_packets = parse_sub_packs(block_bits[start..block_bits.len()].to_vec());

        Packet{
            version: version,
            type_id: type_id,
            length_bit: Some(block_bits[7] as u32),
            length: Some(length),
            literal: None,
            sub_packets: Some(sub_packets),
        }
    }
}

fn transform_to_binary(hex: u32) -> String {
    let first_zero = if hex < 8 {"0"} else {""};
    let second_zero = if hex < 4 {"0"} else {""};
    let third_zero = if hex < 2 {"0"} else {""};

    format!("{0}{1}{2}{3:b}",first_zero, second_zero, third_zero ,hex)
}

fn parse_input(st: &String) -> Vec<u8> {
    st
        .chars()  
        .flat_map(|c| {
            let hex: u32 = c.to_digit(16).unwrap();

            transform_to_binary(hex)
                .chars()
                .flat_map(|c| c.to_digit(2).map(|d| d as u8))
                .collect::<Vec<u8>>()
        })
        .collect()
}

fn main() {
    let mut contents = String::new();
    File::open("../data/16.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");
    
    let input: Vec<u8> = parse_input(&contents);

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_parse() {
        let contents = String::from("D2FE28");
        let inputs = parse_input(&contents);
        assert_eq!(inputs, vec![1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0]); 
    }
    
    #[test]
    fn test_parse_block(){
        let contents = String::from("D2FE28");
        let inputs = parse_input(&contents);
        assert_eq!(parse_block(inputs), Packet{
            version: 6,
            type_id: 4,
            literal: Some(2021),
            length_bit: None,
            length: None,
            sub_packets: None,
        });
    }
}
