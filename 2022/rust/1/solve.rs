use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn read_file() -> Vec<String>{
    let file = File::open("input.txt").expect("Can't open file");
    let buf = BufReader::new(file);
    buf.lines().map(|l| l.expect("Could not read lines")).collect()
}

fn main(){
    let content: Vec<String> = read_file();
    let mut sum : i32 = 0;
    let mut sums : Vec<i32> = Vec::new();
    for i in 0..content.len() {
        let element : &String = &content[i];
        if element.parse::<f64>().is_ok() {
            let number : i32 = content[i].parse().unwrap();
            sum += number;
        }else if !element.parse::<f64>().is_ok(){
            sums.push(sum);
            sum = 0;
        }
    }
    let mut max_sum1 = 0; // I know that this is inefficient.
    let mut max_sum2 = 0;
    let mut max_sum3 = 0;
    for i in 0..sums.len(){
        let present_number : i32 = sums[i];
        if present_number > max_sum1 {
            max_sum3 = max_sum2;
            max_sum2 = max_sum1;
            max_sum1 = present_number;
        }else if present_number > max_sum2{
            max_sum3 = max_sum2;
            max_sum2 = present_number;

        }else if present_number > max_sum3{
            max_sum3 = present_number;

        }
    }
    println!("The first answer was {}", max_sum1);
    println!("The second answer was {} + {} + {} = {}", max_sum1, max_sum2, max_sum3 ,max_sum1+max_sum2+max_sum3);
}
