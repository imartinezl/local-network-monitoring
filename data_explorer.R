library(dplyr)

wifi_files <- list.files(path = 'data', pattern = "wifi_", full.names = T)
devices_files <- list.files(path = 'data', pattern = "devices_", full.names = T)

devices_df <- lapply(devices_files, function(dev){
  t <- substr(dev, 14, 32) %>% as.POSIXct(format="%Y-%m-%dT%H:%M:%S")
  jsonlite::fromJSON(dev) %>% 
    dplyr::mutate(time = t)
}) %>% dplyr::bind_rows()

devices_df %>% 
  dplyr::mutate(time_hour = lubridate::round_date(time, unit="1 hour")) %>% 
  dplyr::group_by(time_hour) %>% 
  dplyr::summarise(n = n_distinct(ipv4)) %>% 
  dplyr::ungroup() %>% 
  ggplot2::ggplot()+
  ggplot2::geom_line(ggplot2::aes(x=time_hour, y=n))
devices_df %>% 
  ggplot2::ggplot()+
  ggplot2::geom_point(ggplot2::aes(x=time, y=ipv4))

wifi_df <- lapply(wifi_files, function(wifi){
  t <- substr(wifi, 11, 29) %>% as.POSIXct(format="%Y-%m-%dT%H:%M:%S")
  jsonlite::fromJSON(wifi) %>% 
    as.data.frame() %>% 
    dplyr::mutate(time = t)
}) %>% dplyr::bind_rows()

wifi_df %>% 
  tidyr::gather(key, value, signal_quality, signal_level_dBm) %>% 
  ggplot2::ggplot()+
  ggplot2::geom_line(ggplot2::aes(x=time, y=as.numeric(value), group=essid), alpha=0.1)+
  ggplot2::geom_line(data = . %>% dplyr::filter(essid %in% c("MOVISTAR_67E6","MOVISTAR_67E6b")), 
                     ggplot2::aes(x=time, y=as.numeric(value), color=essid))+ 
  ggplot2::facet_grid(rows=vars(key), scales="free")+
  ggplot2::labs(x=NULL, y=NULL)+
  ggplot2::theme(legend.position = "top")
  