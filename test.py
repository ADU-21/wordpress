#!/usr/bin/python
# coding: utf-8
import sys 
import MySQLdb

def change_the_option_value_by_ec2_public_ip(public_ip, mysql_host, s3_bucket):
    sql_message1 = "UPDATE wp_options SET option_value='http://"+public_ip+"/wordpress' WHERE option_name='siteurl' OR option_name='home'"
    tantan_wordpress_s3 = 'a:7:{s:17:"post_meta_version";i:3;s:6:"region";s:9:"us-west-1";s:11:"force-https";b:0;s:10:"copy-to-s3";s:1:"1";s:13:"serve-from-s3";s:1:"1";s:6:"bucket";s:17:"'+s3_bucket+'";s:13:"manual_bucket";b:1;}'
    theme_mods_twentyfifteen = 'a:5:{i:0;b:0;s:11:"custom_logo";i:9;s:12:"header_image";s:107:"http://s3-us-west-1.amazonaws.com/'+s3_bucket+'/wordpress/wp-content/uploads/2016/07/09101724/head2.jpg";s:17:"header_image_data";O:8:"stdClass":5:{s:13:"attachment_id";i:15;s:3:"url";s:107:"http://s3-us-west-1.amazonaws.com/'+s3_bucket+'/wordpress/wp-content/uploads/2016/07/09101724/head2.jpg";s:13:"thumbnail_url";s:107:"http://s3-us-west-1.amazonaws.com/'+s3_bucket+'/wordpress/wp-content/uploads/2016/07/09101724/head2.jpg";s:6:"height";i:1300;s:5:"width";i:954;}s:16:"background_image";s:112:"http://s3-us-west-1.amazonaws.com/'+s3_bucket+'/wordpress/wp-content/uploads/2016/07/09102956/backgroud3.jpg";}'
    sql_message2 = "UPDATE wp_options SET option_value='"+tantan_wordpress_s3+"' WHERE option_name='tantan_wordpress_s3'"
    sql_message3 = "UPDATE wp_options SET option_value='"+theme_mods_twentyfifteen+"' WHERE option_name='theme_mods_twentyfifteen'"
    db = MySQLdb.connect(mysql_host,"root","root123456","wordpress")
    cursor = db.cursor()
    try:
        cursor.execute(sql_message1) 
        db.commit()
        cursor.execute(sql_message2)
        db.commit()
        cursor.execute(sql_message3)
        db.commit()
    except Exception as e:
        print "change the option value by ec2 public ip:\n",e
        db.rollback()    
    db.close()

if __name__ == "__main__":
    public_ip = sys.argv[1]
    mysql_host = sys.argv[2] 
    s3_bucket = sys.argv[3]
    change_the_option_value_by_ec2_public_ip(public_ip, mysql_host, s3_bucket)
