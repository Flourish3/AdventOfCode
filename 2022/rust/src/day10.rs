use std::fs::File;
use std::io::prelude::*;

fn get_cycle_and_count(instuction: &str) -> Vec<i32> {
    let v : Vec<&str> = instuction.split(" ").collect();

    match &v[..] {
        ["noop"] => vec![0],
        ["addx", x] => {
            println!("{}", x.parse::<i32>().unwrap());
            vec![0, x.parse::<i32>().unwrap()]},
        _ => vec![]
    }
}

fn main() {
    let mut contents = String::new();
    File::open("../data/day10.txt")
        .expect("File not found")
        .read_to_string(&mut contents)
        .expect("Something went wrong when reading");

    // Cycles 20, 60, 100, 140, 180, 220

    let changes = contents
        .lines()
        .flat_map(|line| get_cycle_and_count(line).into_iter())
        .scan(1, |acc, change| {
            *acc = *acc + change;
            Some(*acc)
        })
        .collect::<Vec<i32>>();


    let crt = changes[..]
        .into_iter()
        .enumerate()
        .map(|(i,&x)| {
            println!("{}, {}", i, ((i+1) % 40));
            if vec![x-1, x, x +1].contains(&(((i+1) % 40) as i32)) {
                "#"
            } else {
                "."
            }
        })
        .collect::<Vec<&str>>();

    println!("{}", crt[0..40].join(""));
    println!("{}", crt[40..80].join(""));
    println!("{}", crt[80..120].join(""));
    println!("{}", crt[120..160].join(""));
    println!("{}", crt[160..200].join(""));
    println!("{}", crt[200..240].join(""));

    println!("{:?}", changes);
    println!("{:?}", crt);

    let twnety = 20*changes[19];
    let sixty = 60*changes[59];
    let hundred = 100*changes[99];
    let hundred_fourty = 140*changes[139];
    let hundred_eighty = 180*changes[179];
    let two_hundred_twenty = 220*changes[219];

    println!("{}", changes.len());
    println!("{}", twnety);
    println!("{}", sixty);
    println!("{}", hundred);
    println!("{}", hundred_fourty);
    println!("{}", hundred_eighty);
    println!("{}", two_hundred_twenty);

    println!("{}", twnety+sixty+hundred+hundred_fourty+hundred_eighty+two_hundred_twenty)

}