# local-network-monitoring

Wi-Fi signal data gathering, analysis and visualization.
The main goal of this project is to check the quality signal and coverage of a local Wi-Fi router.

## Built with

### Wi-Fi data collection

- [iwlist](https://linux.die.net/man/8/iwlist): detailed wireless information from a wireless interface
- [python-iwlist](https://github.com/iancoleman/python-iwlist): python scanner and parser for wireless networks
 
### Connected devices
- [nmap](https://nmap.org/): open source utility for network discovery and security auditing
- [nmap python](https://xael.org/pages/python-nmap-en.html): python library which helps in using nmap port scanner

### Data exploration

- [R](https://www.r-project.org/) - Programming Language / 3.6.0
- [RStudio](https://www.rstudio.com/) - IDE for R / 1.2.1335
- [dplyr](https://dplyr.tidyverse.org/) - A grammar of data manipulation / 0.8.1
- [ggplot2](https://ggplot2.tidyverse.org/) - Create graphics with R / 3.1.1
- [jsonlite](https://github.com/jeroen/jsonlite) - A Robust, High Performance JSON Parser and Generator for R / 1.6
- [lubridate](https://lubridate.tidyverse.org/) - Library for date-times / 1.7.4




sudo iwlist wlan0 scan | egrep "Cell|ESSID|Signal|Rates"

sudo nmap -sP -r 192.168.1.0/24
