#!/usr/share/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd
import sys

try :
    if len(sys.argv[1]) and len(sys.argv[2]) :
        pass
except:
    print "Usage : python2 bot_v2.py 'excel file name' 'brand name'"
    exit()
#+++++++++++++++++++++ Excel Magic here+++++++++++++++++++++++#

a = xlrd.open_workbook(sys.argv[1])
b = a.sheet_by_index(0)

i=0
j=0
dic = {}
while True:
    try:
        i=i+1
        j=j+1
        if b.cell(i,1).value :
            dic[str(b.cell(i,1).value)]=str(b.cell(j,2).value)
            #print "{} => {}".format(b.cell(i,1).value,b.cell(j,2).value)
    except:
        break
print "intialising stuff"
print "hacking nasa with html"
print "Area 51 HACK completed\n"



#++++++++++++++++++++++++++web magic here++++++++++++++++++++++++++++++++#
f = webdriver.Firefox()

#-----------loging in---------------------#
f.get('https://tvnama.com/wp-login.php')
a = f.find_element_by_name('log')
a.clear()
a.send_keys('username')
a = f.find_element_by_name('pwd')
a.clear()
a.send_keys('password')
a = f.find_element_by_name('wp-submit')
a.click()


#-----------------doing the cool shit----------#
f.get('https://tvnama.com/wp-admin/post-new.php?post_type=product')

b = f.find_elements_by_class_name('button.tagadd')

#-----------------------------------------------------------------#
a = f.find_element_by_id('mlx_tvnama_product_spcf_general_model')
a.clear()
a.send_keys(dic['Model'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_general_series')
a.clear()
a.send_keys(dic['Series'])


a = f.find_element_by_id('mlx_tvnama_product_spcf_general_other_names')
a.clear()
a.send_keys(dic['Other Names'])


a = f.find_element_by_id('mlx_tvnama_product_spcf_general_smart_tv')
a.clear()
a.send_keys(dic['Smart TV'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_general_3d_tv')
a.clear()
a.send_keys(dic['3D TV'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_launch_year')
a.clear()
a.send_keys(dic['Launch Time'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_body_curved_flat_screen')
a.clear()
a.send_keys(dic['Curved/Flat screen'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_body_display_size')
a.clear()
a.send_keys(dic['Display Size'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_body_dimension_with_stand')
a.clear()
a.send_keys(dic['Dimensions - W x H (with stand) '])

a = f.find_element_by_id('mlx_tvnama_product_spcf_body_dimension_without_stand')
a.clear()
a.send_keys(dic['Dimensions - W x H (without stand)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_body_tv_thickness')
a.clear()
a.send_keys(dic['TV Thickness'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_weight_with_stand')
a.clear()
a.send_keys(dic['Weight (with stand)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_weight_without_stand')
a.clear()
a.send_keys(dic['Weight (without stand)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_resolution')
a.clear()
a.send_keys(dic['Resolution'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_panel_type')
a.clear()
a.send_keys(dic['Panel Type'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_backlight_type')
a.clear()
a.send_keys(dic['Backlight Type'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_backlight_arrangement')
a.clear()
a.send_keys(dic['Backlight Arrangement'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_contrast_ratio')
a.clear()
a.send_keys(dic['Contrast Ratio'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_brightness')
a.clear()
a.send_keys(dic['Brightness (cd/m2)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_color')
a.clear()
a.send_keys(dic['Color'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_refresh_rate')
a.clear()
a.send_keys(dic['Refresh Rate'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_response_time')
a.clear()
a.send_keys(dic['Response Time (G to G)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_pic_qlty_viewing_angle')
a.clear()
a.send_keys(dic['Viewing Angle (H/V)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_aud_qlty_sound_system')
a.clear()
a.send_keys(dic['Sound System'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_aud_qlty_no_of_speakers')
a.clear()
a.send_keys(dic['# of Speakers'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_aud_qlty_total_speaker_output')
a.clear()
a.send_keys(dic['Total Speaker Output'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_aud_qlty_subwoofer')
a.clear()
a.send_keys(dic['Subwoofer'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_feat_hdr')
a.clear()
a.send_keys(dic['HDR'])

# No BlackLight Dimming in Excel sheets


#a = f.find_element_by_id('mlx_tvnama_product_spcf_feat_local_dimming')
#a.clear()
#a.send_keys(dic['Backlight Dimming'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_feat_motion_interpolation')
a.clear()
a.send_keys(dic['Motion Interpolation'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_feat_wi_fi_direct')
a.clear()
a.send_keys(dic['WiFi Direct'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_feat_screen_mirroring')
a.clear()
a.send_keys(dic['Screen Mirroring'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_feat_others')
a.clear()
a.send_keys(dic['Others'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_os')
a.clear()
a.send_keys(dic['Operating System'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_cpu')
a.clear()
a.send_keys(dic['CPU'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_gpu')
a.clear()
a.send_keys(dic['GPU'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_hard_disk')
a.clear()
a.send_keys(dic['Hard Disk'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_ram')
a.clear()
a.send_keys(dic['RAM'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_inbuilt_apps')
a.clear()
a.send_keys(dic['Inbuilt apps '])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_wi_fi_built_in')
a.clear()
a.send_keys(dic['WiFi Built-In'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_bluetooth')
a.clear()
a.send_keys(dic['Bluetooth'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_smart_tv_ethernet_lan')
a.clear()
a.send_keys(dic['Ethernet/LAN'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_3d_tv_3d_type')
a.clear()
a.send_keys(dic['3D Type'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_3d_tv_2d_to_3d_conversion')
a.clear()
a.send_keys(dic['2D to 3D conversion & vice-versa'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_usb')
a.clear()
a.send_keys(dic['USB'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_hdmi')
a.clear()
a.send_keys(dic['HDMI'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_component_video_in')
a.clear()
a.send_keys(dic['Component Video In (YPbPr)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_composite_video_in')
a.clear()
a.send_keys(dic['Composite Video In'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_digital_optical_audio_output')
a.clear()
a.send_keys(dic['Digital Optical Audio Out (SPDIF)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_digital_coaxial_audio_output')
a.clear()
a.send_keys(dic['Digital Coaxial Audio Out (SPDIF)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_analog_audio_out_3_5_mm_jack')
a.clear()
a.send_keys(dic['Analog Audio Out - 3.5mm Jack (Headphone)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_analog_audio_out_line_out')
a.clear()
a.send_keys(dic['Analog Audio Out - Line out (AUX)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_analog_audio_out_rca')
a.clear()
a.send_keys(dic['Analog Audio Out - RCA'])


a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_analog_audio_in_rca')
a.clear()
a.send_keys(dic['Analog Audio In - RCA'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_coaxial_rf')
a.clear()
a.send_keys(dic['Coaxial RF (Cable/Antenna)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_vga_port')
a.clear()
a.send_keys(dic['VGA Port (PC Input)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_av_out')
a.clear()
a.send_keys(dic['AV Out'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_conn_sd_card_slot')
a.clear()
a.send_keys(dic['SD Card Slot'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_supp_form_audio')
a.clear()
a.send_keys(dic['Audio'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_supp_form_video')
a.clear()
a.send_keys(dic['Video'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_supp_form_multimedia_codecs')
a.clear()
a.send_keys(dic['Multimedia Codecs'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_supp_form_video_signal_support')
a.clear()
a.send_keys(dic['Video Signal Support'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_supp_form_images')
a.clear()
a.send_keys(dic['Images'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_supp_form_subtitles')
a.clear()
a.send_keys(dic['Subtitle'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_miscl_power_consumption')
a.clear()
a.send_keys(dic['Power Consumption'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_miscl_power_consumption_standby')
a.clear()
a.send_keys(dic['Power Consumption (Standby)'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_miscl_warranty')
a.clear()
a.send_keys(dic['Warranty'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_miscl_remote_type')
a.clear()
a.send_keys(dic['Remote type'])

a = f.find_element_by_id('mlx_tvnama_product_spcf_miscl_accessories')
a.clear()
a.send_keys(dic['Accessories (In box)'])


#---------------------------------------------------------------#

#-----------------adding brand tag-------------#
a = f.find_element_by_id('new-tag-brand')
a.clear()
a.send_keys(sys.argv[2])
a = b[0]
a.click()

#-----------------adding resolution tag-------------#
a = f.find_element_by_id('new-tag-resolution')
a.clear()
if "4k" in dic['Resolution']:
    a.send_keys('Ultra HD (4k)')
else:
    a.send_keys(dic['Resolution'][:-14])
a = b[2]
a.click()


#--------------adding No. USB PORTS-------------------#
a = f.find_element_by_id('new-tag-usb_ports')
a.clear()
if dic['USB'] >= 3:
    a.send_keys('3 and above')
else:
    a.send_keys(dic['USB'])
a = b[6]
a.click()

#--------------adding No. HDMI PORTS-------------------#
a = f.find_element_by_id('new-tag-hdmi_ports')
a.clear()
if dic['HDMI'] >= 3:
    a.send_keys('3 and above')
else:
    a.send_keys(dic['HDMI'])
a = b[7]
a.click()
#--------------adding warranty-------------------#
a = f.find_element_by_id('new-tag-warranty')
a.clear()
a.send_keys(dic['Warranty'])
a = b[8]
a.click()
#--------------adding launch year-------------------#
a = f.find_element_by_id('new-tag-launch_year')
a.clear()
a.send_keys(dic['Launch Time'][:-2])
a = b[9]
a.click()
