use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::str::FromStr;
use std::time::Instant;

fn read_file(filename : &str) -> Vec<String>{
    let file = File::open(filename).expect("Can't open file");
    let buf = BufReader::new(file);
    let data : Vec<String> = buf.lines().map(|l| l.expect("Could not read lines")).collect();
    return data;

}

fn adapt_data(data : &Vec<String>) -> Vec<(u32, u32, u32, u32)> {
    let mut data_vector : Vec<(u32, u32, u32 , u32)> = Vec::new();
    for i in 0 .. data.len(){
        let element : &String = &data[i];
        let sep1 : Vec<&str> = element.split(",").collect();
        let (first, second) : (String, String) = (sep1[0].to_string(), sep1[1].to_string());
        let s1 : Vec<&str> = first.split("-").collect();
        let s2 : Vec<&str> = second.split("-").collect();
        let u1 : u32 = FromStr::from_str(s1[0]).unwrap();
        let u2 : u32 = FromStr::from_str(s1[1]).unwrap();
        let u3 : u32 = FromStr::from_str(s2[0]).unwrap();
        let u4 : u32 = FromStr::from_str(s2[1]).unwrap();
        data_vector.push((u1, u2, u3, u4));

    }
    return data_vector;
}

fn compare_1(a : &u32, b : &u32, x : &u32, y : &u32) -> u32{
    if a <= x && b >= y {
        return 1;
    }
    else if x <= a && y >= b{
        return 1;
    }
    else{
        return 0;
    }
}

fn compare_2(a : &u32, b : &u32, x : &u32, y : &u32) -> u32{
    if a <= x && b >= y {
        return 1;
    }
    else if x <= a && y >= b{
        return 1;
    }
    else if x <= b && x >= a{
        return 1;
    }
    else if b <= x && a >= x{
        return 1;
    }
    else if y >= a && y <= b{
        return 1;
    }
    else if a >= y && b <= y{
        return 1;
    }
    else if a == y{
        return 1;
    }
    else{
        return 0;
    }

}

fn solve(adapted_data : &Vec<(u32, u32, u32, u32)>) -> (u32, u32){
    let mut s1 : u32 = 0;
    let mut s2 : u32 = 0;
    for i in 0 .. adapted_data.len(){
        let e : (u32, u32, u32, u32) = adapted_data[i];
        let a : u32 = e.0;
        let b : u32 = e.1;
        let x : u32 = e.2;
        let y : u32 = e.3;
        s1 += compare_1(&a, &b, &x, &y);
        s2 += compare_2(&a, &b, &x, &y);
    }
    return (s1, s2);
}

fn main(){
    let start = Instant::now();
    let data : Vec<String> = read_file("input.txt");
    let data_vec : Vec<(u32, u32, u32, u32)> = adapt_data(&data);
    let solutions : (u32, u32) = solve(&data_vec);
    let duration = start.elapsed();
    println!("The first answer is {}, and the second is {}", solutions.0, solutions.1);
    println!("The time was {:?}", duration);
}
