#include <stdio.h>
#include <gpiod.h>
#include <unistd.h>

#define line_num 2

//set up struct (includes get line struct)
//make array; the line part is null
//asign value via for loop
//check for signals

struct gpio_pin { // creating struct for a single gpio pin
    int pin_num;
    struct gpiod_line *line; 
};

int main() {
    
    int ret;
    struct gpiod_chip *chip;
    struct gpio_pin pins[] = {{18, NULL},{17, NULL}}; // instantiating the pins

    chip = gpiod_chip_open_by_name("gpiochip0"); //opening chip + verification
    if (!chip) {
        perror("Open chip failed");
        return 1;
    }

    for (int i = 0; i < line_num; i++) { //assigning lines to instantiated gpio_pins
        pins[i].line = gpiod_chip_get_line(chip, pins[i].pin_num);
        if (!pins[i].line) {
            perror("Get line failed");
            gpiod_chip_close(chip);
            return 1;
        }
    }

    for (int i = 0; i < line_num; i++) { //request procedure as per the gpiod.h library
        ret = gpiod_line_request_input(pins[i].line, "gpio-example");
        if (ret < 0) {
            perror("Request line as input failed");
            gpiod_chip_close(chip);
            return 1;
        }
    }

    while (1) { 
        int value_17, value_18;
        int vals[line_num];

        for (int i = 0; i < line_num; i++) { //reading gpio signals
            vals[i] = gpiod_line_get_value(pins[i].line);
            if (vals[i] < 0) {
                perror("Read line input failed");
                gpiod_chip_close(chip);
                return 1;
            }
        }

        value_18 = vals[0];
        value_17 = vals[1];

        if (value_17 && value_18) {
            printf("3\n"); // Both signals received
        } else if (value_17) {
            printf("2\n"); // Signal on GPIO 17 received
        } else if (value_18) {
            printf("1\n"); // Signal on GPIO 18 received
        } else {
            printf("0\n"); // No signal received on either GPIO
        }

        usleep(100000); // Sleep for 100ms to avoid busy waiting
    }

    gpiod_chip_close(chip);
    return 0;
}
