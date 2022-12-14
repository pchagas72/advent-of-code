use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::collections::HashMap;
use std::time::Instant;

fn read_file(filename : &str) -> Vec<String> {
    let file = File::open(filename).expect("Cant open file");
    let buf = BufReader::new(file);
    let data : Vec<String> = buf.lines().map(|l| l.expect("Could not read lines")).collect();
    return data;
}

fn create_hashmap() -> HashMap<String, u32> {
    let mut hashmap : HashMap<String, u32> = HashMap::new();
    let letters : Vec<char> = Vec::from(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']);
    let mut u_letters : Vec<char> = Vec::new();
    for i in 0 .. letters.len(){
        let ch : Vec<char> = letters[i].to_uppercase().collect();
        u_letters.push(ch[0]);
    }
    let mut counter : u32 = 1;
    for i in 0 .. letters.len(){
        hashmap.insert(letters[i].to_string(), counter);
        counter += 1;
    }
    for i in 0 .. u_letters.len(){
        hashmap.insert(u_letters[i].to_string(), counter);
        counter += 1;
    }
    return hashmap;
}

fn divide_sacks(data : &Vec<String>) -> Vec<(String, String)> {
    let mut divided : Vec<(String, String)> = Vec::new();
    for i in 0 .. data.len(){
        let element : String = data[i].to_string();
        let element_len = element.len();
        let l = element_len/2;

        let mut first_string : String = String::new();
        let mut second_string : String = String::new();

        for (i, c) in element.chars().enumerate(){
            if i+1 <= l {
               first_string.push(c);
            }
            else if i+1 > l {
               second_string.push(c);
            }
        }
        divided.push((first_string, second_string));
    }
    return divided;
}

fn divide_equals(divided_data : Vec<(String, String)>) -> Vec<char> {
    let mut equals : Vec<char> = Vec::new();
    for i in 0 .. divided_data.len(){
        let first : Vec<char> = divided_data[i].0.to_string().chars().collect();
        let second : Vec<char> = divided_data[i].1.to_string().chars().collect();

        let mut added_element : char = '_';

        for i in 0 .. first.len(){
            let element : char = first[i];
            if second.contains(&element){
                if element != added_element {
                    equals.push(element);
                    added_element = element;
                }
                //break; // I don't like this, bcs if the problem had more than one equal it would not detect. But I could to make it a bit faster
            }
        }

    }
    return equals;
}

fn sum_char_values(values : Vec<char>, cases : &HashMap<String, u32>) -> u32{ // Just now I noticed that I created the hashmap with String keys, and not char keys, it's 1:11AM.
    let mut sum : u32 = 0;
    for i in 0 .. values.len(){
        let key : String = values[i].to_string();
        let value : u32 = cases[&key]; // Now I see that I should have used a &char as key.
        sum += value;
    }
    return sum;
}

fn divide_groups(data : &Vec<String>) -> (Vec<String>, Vec<String>, Vec<String>){
    let mut gs1 : Vec<String> = Vec::new();
    let mut gs2 : Vec<String> = Vec::new();
    let mut gs3 : Vec<String> = Vec::new();
    let mut counter : u32 = 0;
    for i in 0 .. data.len(){
        let element : &String = &data[i];
        if counter == 0{
            gs1.push(element.to_string());
            counter += 1
        }
        else if counter == 1{
            gs2.push(element.to_string());
            counter += 1;
        }
        else if counter == 2{
            gs3.push(element.to_string());
            counter = 0;
        }
    }
    return (gs1, gs2, gs3);
}

fn get_common_values(divided_groups : (Vec<String>, Vec<String>, Vec<String>)) -> Vec<char>{
    let mut commons : Vec<char> = Vec::new();
    let (g1, g2, g3) : (Vec<String>, Vec<String>, Vec<String>) = divided_groups;
    for i in 0 .. g1.len(){
        let first : Vec<char> = g1[i].to_string().chars().collect();
        let second : Vec<char> = g2[i].to_string().chars().collect();
        let third : Vec<char> = g3[i].to_string().chars().collect();
        for i in 0 .. first.len(){
            let element : char = first[i];
            if second.contains(&element) && third.contains(&element){
                commons.push(element);
                break;
            }
        }
    }
    return commons;
}

fn main(){
    let start = Instant::now();
    let cases : HashMap<String, u32> = create_hashmap();
    let data : Vec<String> = read_file("test.txt");
    let divided : Vec<(String, String)> = divide_sacks(&data);
    let equals : Vec<char> = divide_equals(divided);
    let first_answer : u32 = sum_char_values(equals, &cases);
    println!("The first answer was {}", first_answer);
    let dg : (Vec<String>, Vec<String>, Vec<String>) = divide_groups(&data);
    let cv : Vec<char> = get_common_values(dg);
    let second_answer : u32 = sum_char_values(cv, &cases);
    let duration = start.elapsed();
    println!("The second answer was {}", second_answer);
    println!("The time was {:?}", duration);
}
