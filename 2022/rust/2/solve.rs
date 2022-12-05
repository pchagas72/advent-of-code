use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::collections::HashMap;

fn read_file(filename : &str) -> Vec<String>{
    let file = File::open(filename).expect("Can't open file");
    let buf = BufReader::new(file);
    buf.lines().map(|l| l.expect("Could not read lines")).collect()
}

fn create_hashmaps() -> ( HashMap<String, u32> , HashMap<String, u32> ) {
    let cases1 : HashMap<String, u32> = HashMap::from([
      ("AX".to_string() , 4),
      ("AY".to_string() , 8),
      ("AZ".to_string() , 3),
      ("BX".to_string() , 1),
      ("BY".to_string() , 5),
      ("BZ".to_string() , 9),
      ("CX".to_string() , 7),
      ("CY".to_string() , 2),
      ("CZ".to_string() , 6),
    ]);

    let cases2 : HashMap<String, u32> = HashMap::from([
      ("AX".to_string() , 3),
      ("AY".to_string() , 4),
      ("AZ".to_string() , 8),
      ("BX".to_string() , 1),
      ("BY".to_string() , 5),
      ("BZ".to_string() , 9),
      ("CX".to_string() , 2),
      ("CY".to_string() , 6),
      ("CZ".to_string() , 7),
    ]);

    return (cases1, cases2);
}

fn solve(data : &Vec<String>, cases : HashMap<String, u32>) -> u32 {
    let mut points : u32 = 0;

    for i in 0 .. data.len(){
        let element : &str = &data[i];
        let element_key : String = element.replace(' ', "");
        let adition : u32 = cases[&element_key];
        points += adition;
    }
    return points;

}

fn main(){
    let data : Vec<String> = read_file("input.txt");
    let (cases1, cases2) : (HashMap<String, u32>, HashMap<String, u32>) = create_hashmaps();
    let first_a : u32 = solve(&data, cases1);
    let second_a : u32 = solve(&data, cases2);
    println!("The first answer is {}", first_a);
    println!("The second answer is {}", second_a);

}
