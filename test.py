#!/usr/bin/python
# coding: utf-8
import sys 
import MySQLdb

def change_the_option_value_by_ec2_public_ip(public_ip, mysql_host):
    sql_message = "UPDATE wp_options SET option_value='http://"+public_ip+"/wordpress' WHERE option_name='siteurl' OR option_name='home'"
    db = MySQLdb.connect(mysql_host,"root","root123456","wordpress")
    cursor = db.cursor()
    try:
        cursor.execute(sql_message) 
        db.commit()
    except Exception as e:
        print "change the option value by ec2 public ip:\n",e
        db.rollback()    
    db.close()

if __name__ == "__main__":
    public_ip = sys.argv[1]
    try: mysql_host = sys.argv[2] 
    except: mysql_host = "testwordpress.ce7ceraac6av.us-west-1.rds.amazonaws.com"
    change_the_option_value_by_ec2_public_ip(public_ip, mysql_host)
