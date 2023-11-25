//#![feature(test)]

//extern crate test;

use std::fs::File;
use std::io::prelude::*;
use std::collections::HashMap;

fn print_error(found: char, expected: char) -> () {
    println!("Found {0}, exptected {1}", found, expected);
}

fn get_auto_complete_score(line: &Vec<char>) -> u64 {
    let mut buffer: Vec<char> = Vec::with_capacity(line.len());
    let mut matching: HashMap<char,char> = HashMap::new();
    matching.insert('}', '{');
    matching.insert('>', '<');
    matching.insert(']', '[');
    matching.insert(')', '(');

    let mut matching_opposite: HashMap<char,char> = HashMap::new();
    matching_opposite.insert('{', '}');
    matching_opposite.insert('<', '>');
    matching_opposite.insert('[', ']');
    matching_opposite.insert('(', ')');

    for c in line {
        if *c == '[' || *c == '(' || *c == '{' || *c == '<' {
            buffer.push(*c);
        } else {
            if buffer[buffer.len() - 1] == *matching.get(c).unwrap() {
                buffer.pop();
            }
        }
    }

    let mut score_map: HashMap<char, u64> = HashMap::new();
    score_map.insert(')', 1);
    score_map.insert(']', 2);
    score_map.insert('}', 3);
    score_map.insert('>', 4);


    buffer.reverse();

    buffer
        .iter()
        .flat_map(|c| matching_opposite.get(&c))
        .fold(0, |acc, val| acc * 5 +  score_map.get(&val).unwrap())
}

fn find_auto_complete_score(input: &Vec<Vec<char>>) -> u64 {
    let mut scores = input
        .iter()
        .filter(|line| find_illegal(line).is_none())
        .map(|line| get_auto_complete_score(line))
        .collect::<Vec<u64>>();
    
    scores.sort();

    println!("{:?}",scores);

    scores[scores.len() / 2]
}

fn get_illegal_score(input: Vec<Vec<char>>) -> u32 {
    let mut score_map: HashMap<char, u32> = HashMap::new();
    score_map.insert(')', 3);
    score_map.insert(']', 57);
    score_map.insert('}', 1197);
    score_map.insert('>', 25137);

    input
        .iter()    
        .flat_map(|line| find_illegal(line))
        .map(|illegal| *score_map.get(&illegal).unwrap())
        .sum()
}

fn find_illegal(line: &Vec<char>) -> Option<char> {
    let mut buffer: Vec<char> = Vec::with_capacity(line.len());
    let mut matching: HashMap<char,char> = HashMap::new();
    matching.insert('}', '{');
    matching.insert('>', '<');
    matching.insert(']', '[');
    matching.insert(')', '(');

    for c in line {
        if *c == '[' || *c == '(' || *c == '{' || *c == '<' {
            buffer.push(*c);
        } else {
            if buffer[buffer.len() - 1] == *matching.get(c).unwrap() {
                buffer.pop();
            } else {
                print_error(*c, buffer[buffer.len()-1]); 
                return Some(*c);
            } 
        }
    }

    None
}

fn parse_input(st: &String) -> Vec<Vec<char>> {
    st
        .lines()
        .map(|l| l.chars().collect())
        .collect()
}

fn main() {
    let mut contents = String::new();
    File::open("../data/10.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");
    
    let input = parse_input(&contents);


    //println!("Part 1 {:?}", get_illegal_score(input));
    println!("Part 2 {}", find_auto_complete_score(&input));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example() {
        let contents = String::from("[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]");
        let inputs = parse_input(&contents);
        assert_eq!(get_illegal_score(inputs), 26397); 
    }

    #[test]
    fn test_part_two(){
        let contents = String::from("[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]");
        let inputs = parse_input(&contents);
        assert_eq!(find_auto_complete_score(&inputs), 288957); 
    }

    #[test]
    fn test_one_input(){
        let contents = String::from("[[<{<{{{([[{[[{}()]<<>{}>]}{{<(){}>{<>}}{{<><>}{<><>}}}][[<<()[]>(<>())>[(())([]())]>]])<{");
        let inputs = parse_input(&contents);
        assert_eq!(get_illegal_score(inputs), 25137); 
    }

}
