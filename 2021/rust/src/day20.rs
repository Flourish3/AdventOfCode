use std::cmp;
use rand::Rng;

fn main() {
    let mut p1 = 0;
    let mut p2 = 0;

    for _ in 0..1000000 {

        //let mut die = (1..=100).cycle();
        let mut player_one_score = 0;
        let mut player_two_score = 0;
    
        let mut player_one_place = 4 - 1;
        let mut player_two_place = 8 - 1;
    
        //let mut die_roll = 0;
        let mut rng = rand::thread_rng();
    
        while player_one_score < 21 && player_two_score < 21 {
            player_one_place = (player_one_place + rng.gen_range(1..=3) + rng.gen_range(1..=3) + rng.gen_range(1..=3)) % 10;
            player_one_score += player_one_place + 1;
            //die_roll += 3;
    
            if player_one_score >= 21{
                break;
            }
    
            player_two_place = (player_two_place + rng.gen_range(1..=3) + rng.gen_range(1..=3) + rng.gen_range(1..=3)) % 10;
            player_two_score += player_two_place + 1;
            //die_roll += 3;
        }

        if player_one_score > player_two_score {
            p1 += 1;
        } else {
            p2 += 1;
        }

    }

    println!("p1 {} p2 {}, perc {}", p1, p2, p1 as f64 /p2 as f64);



   // println!("die roll: {}, player one: {}, player two: {}, ans: {}", die_roll, player_one_score, player_two_score,  die_roll*cmp::min(player_one_score, player_two_score))

}