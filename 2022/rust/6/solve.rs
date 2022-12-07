use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn read_file(filename : &str) -> String{
    let file = File::open(filename).expect("Could not open file");
    let buf = BufReader::new(file);
    let n_data : String = buf.lines().map(|l| l.expect("Could not read lines")).collect::<String>();
    return n_data;
}

fn check_different(v : &mut Vec<char>, size : usize) -> bool {
    let mut v2 : Vec<char> = Vec::new();
    for item in 0 .. v.len(){
        v2.push(v[item]);
    }
    let mut counter = 0;
    for i in 0 .. v.len(){
        let current_element : char = v[i];
        if v.len() != size{
            return false;
        }
        for k in 0 .. v2.len(){
            if current_element == v2[k]{
                counter += 1;
            }
        }
    }

    if counter == size{
        return true;
    }
    v.remove(0);
    return false;
// This function above checks if all elements in an vector are different.
// if they are, it returns (vector, true).
// if they are not, it removes the first element of the vector and returns (newVector, false)
}

fn detect_signal(n_data : &String, tom : &str) -> usize{
    let mut size : usize = 0;
    if tom == "message" { size = 14; }
    if tom == "packet" { size = 4; }
    let mut chars : Vec<char> = Vec::new();
    let mut temp : Vec<char> = Vec::new();
    let v_ndata : Vec<char> = n_data.chars().collect();
    for i in 0 .. v_ndata.len(){
        let element : char = v_ndata[i];
        chars.push(element);
        temp.push(element);
        let y : bool = check_different(&mut temp, size);
        if y == true{
            return chars.len();
        }
    }
    return chars.len();

}

fn main(){

    let data : String = read_file("input.txt");
    let a : usize = detect_signal(&data, "packet");
    let b : usize = detect_signal(&data, "message");
    println!("The first answer was {}", a);
    println!("The second answer was {}", b);

}
