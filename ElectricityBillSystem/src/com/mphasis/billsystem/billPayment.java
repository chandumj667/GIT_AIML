package com.mphasis.billsystem;

public class billPayment {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int units = 280;
		double bill = 0;
		if(units<100) {
			bill = units * 1.20;
		}
		else if(units<300) {
			bill = 100 * 1.20 + (units - 100)*2;
		}
		System.out.println("Bill to be paid for consumption  of "+units+" units is: "+ bill);
	}

}
