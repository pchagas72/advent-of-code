package main;

import "fmt"
import "bufio"
import "os"
import "strconv"


func read_file(path string) ([]string, error) {

	file, err := os.Open(path);
	if err != nil {
		return nil, err;
	}
	defer file.Close();

	var lines []string;
	scanner := bufio.NewScanner(file);
	for scanner.Scan() {

		lines = append(lines, scanner.Text());

	}
	return lines, scanner.Err();

}

func check_error(e error){

	if e != nil{
		panic(e);
	}

}

func return_digit_list(data []string) ([][]string) {

	var counter int = 0;

	var return_list [][]string;

	for counter < len(data){

		var element string = data[counter];
		chars := []rune(element);

		var tamanho_do_numero int = len(chars);
		if (counter == 0){

			for digito := 0; digito < tamanho_do_numero; digito++{

				var lista_digito_ordem []string;
				return_list = append(return_list, lista_digito_ordem);

			}
		}

		var i int = 0;
		for i<len(chars) {
			char := string(chars[i]);
			return_list[i] = append(return_list[i], char);
			i++;

		}
		counter++

	}
	return return_list;
}

func process_digit_list(digit_lists [][]string) (string, string){

	var gamma_rate string;
	var epsilon_rate string;

	for counter := 0; counter < len(digit_lists); counter++{

		var digit_list []string = digit_lists[counter];
		var ones int = 0;
		var zeroes int = 0;
		for i:= 0; i < len(digit_list); i++{
			if(digit_list[i] == "0") {zeroes += 1};
			if(digit_list[i] == "1") {ones += 1};
		}
		if (ones > zeroes) { gamma_rate = gamma_rate + "1"; epsilon_rate = epsilon_rate + "0" };
		if (zeroes > ones) { gamma_rate = gamma_rate + "0"; epsilon_rate = epsilon_rate + "1" };

	}
	return gamma_rate, epsilon_rate;
}

func binary_to_decimal(bin_num string) (int64){

	num, err := strconv.ParseInt(bin_num, 2, 64);
	check_error(err);
	return num;

}

func return_answer(gamma_rate int, epsilon_rate int) (int) { return gamma_rate * epsilon_rate }

func main(){

	//test_array, err := read_file("../data/3st_test.txt");
	def_array, new_err := read_file("../data/3st.txt");
	//check_error(err);
	check_error(new_err);
	
	var digit_list [][]string = return_digit_list(def_array);
	gamma_rate_string, epsilon_rate_string := process_digit_list(digit_list);

	gamma_rate := binary_to_decimal(gamma_rate_string);
	epsilon_rate := binary_to_decimal(epsilon_rate_string);

	var answer = return_answer(int(gamma_rate), int(epsilon_rate));
	fmt.Println(answer);

}
