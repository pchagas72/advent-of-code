
// I know that this is a pretty bad code, but come on, it's my first day with go :'(

package main

import "fmt"
import "bufio"
import "os"

func readLines(path string) ([]string, error) {
        file, err := os.Open(path);
        if err != nil {
                return nil, err;
        };
        defer file.Close()

        var lines []string;
        scanner := bufio.NewScanner(file);
        for scanner.Scan() {

                lines = append(lines, scanner.Text());

        }
        return lines, scanner.Err()
}

func check_error(e error){

	if e != nil {
		panic(e);
	};

}

func main() {

	test_data, err := readLines("../data/3st.txt");
	check_error(err);
	fmt.Println(test_data);

	var counter int = 0;
	var one_ds []string;  // First digit list, and so on
	var two_ds []string;
	var tree_ds []string;
	var four_ds []string;
	var five_ds []string;
	var six_ds []string;
	var seven_ds []string;
	var eight_ds []string;
	var nine_ds []string;
	var ten_ds []string;
	var eleven_ds []string;
	var twelve_ds []string;

	for counter < len(test_data) {

		var element string = test_data[counter];
		var first_digit string = string(element[0]);
		var second_digit string = string(element[1]);
		var third_digit string = string(element[2]);
		var fourth_digit string = string(element[3]);
		var fifth_digit string = string(element[4]);
		var sixth_digit string = string(element[5]);
		var seventh_digit string = string(element[6]);
		var eight_digit string = string(element[7]);
		var nineth_digit string = string(element[8]);
		var tenth_digit string = string(element[9]);
		var eleventh_digit string = string(element[10]);
		var twelth_digit string = string(element[11]);

		one_ds =  append(one_ds, first_digit);
		two_ds =  append(two_ds, second_digit);
		tree_ds = append(tree_ds, third_digit);
		four_ds = append(four_ds, fourth_digit);
		five_ds = append(five_ds, fifth_digit);
		six_ds =  append(six_ds, sixth_digit);
		seven_ds =  append(seven_ds, seventh_digit);
		eight_ds = append(eight_ds, eight_digit);
		nine_ds = append(nine_ds, nineth_digit);
		ten_ds = append(ten_ds, tenth_digit);
		eleven_ds = append(eleven_ds, eleventh_digit);
		twelve_ds = append(twelve_ds, twelth_digit);

		counter++;
	}

	var gamma_rate []string;
	var epsilon_rate []string;

	var ones, zeroes int;

		for i := 0; i <= 11; i++{

		if i == 0{ 
			ones, zeroes = return_digit(one_ds); 
		}else if i == 1{
			ones, zeroes = return_digit(two_ds); 
		}else if i == 2{ 
			ones, zeroes = return_digit(tree_ds);
		}else if i == 3{
			ones, zeroes = return_digit(four_ds);
		}else if i == 4 {
			ones, zeroes = return_digit(five_ds);
		}else if i == 5 {
			ones, zeroes = return_digit(six_ds);
		} else if i == 6 {
			ones, zeroes = return_digit(seven_ds);
		} else if i == 7 {
			ones, zeroes = return_digit(eight_ds);
		} else if i == 8 {
			ones, zeroes = return_digit(nine_ds);
		} else if i == 9 {
			ones, zeroes = return_digit(ten_ds);
		} else if i == 10 {
			ones, zeroes = return_digit(eleven_ds);
		} else {
			ones, zeroes = return_digit(twelve_ds);
		}

		if ones > zeroes { gamma_rate = append(gamma_rate, "1"); epsilon_rate = append(epsilon_rate, "0"); };
		if zeroes > ones { gamma_rate = append(gamma_rate, "0"); epsilon_rate = append(epsilon_rate, "1"); };
	}

	fmt.Println(gamma_rate);
	fmt.Println(epsilon_rate);


}

func return_digit(digit_list []string) (int, int){

	var ones int = 0;
	var zeroes int = 0;

	for i := 0; i < len(digit_list); i++{

		var element string = digit_list[i];
		if element == "0" { zeroes++ };
		if element == "1" { ones++ };
	}

	return ones, zeroes;

}






















