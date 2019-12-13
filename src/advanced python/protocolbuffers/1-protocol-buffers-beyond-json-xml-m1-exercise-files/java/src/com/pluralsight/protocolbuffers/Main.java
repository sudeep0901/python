package com.pluralsight.protocolbuffers;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class Main {

    public static void main(String[] args) {
	    Customer customer = new Customer();
        customer.setFirstName("Fred");
        customer.setLastName("Thompson");

        Address address = new Address();
        address.setAddress1("123 Market St");
        address.setAddress2("");
        address.setCity("Houston");
        address.setState("Texas");
        address.setZipCode("77001");

        customer.setAddress(address);

        CustomerProtoBuf.CustomerPB customerPB = CustomerProtoBuf.CustomerPB.newBuilder()
                .setFirstName(customer.getFirstName())
                .setLastName(customer.getLastName())
                .setAddress(CustomerProtoBuf.AddressPB.newBuilder()
                    .setAddress1(address.getAddress1())
                    .setAddress2(address.getAddress2())
                    .setCity(address.getCity())
                    .setState(address.getState())
                    .setZipCode(address.getZipCode())
                    .build())
                .build();

        long startTime;
        long endTime;
        int iterations = 1000;
        int i;
        int size = 0;

        startTime = System.currentTimeMillis();
        for (i = 0; i < iterations; i++) {
            size = xmlTest(customer);
        }
        endTime = System.currentTimeMillis();

        System.out.println("XML marshall / unmarshall: " + Long.toString(endTime - startTime) + " ms");
        System.out.println("XML Size: " + Integer.toString(size));

        startTime = System.currentTimeMillis();
        for (i = 0; i < iterations; i++) {
            size = jsonTest(customer);
        }
        endTime = System.currentTimeMillis();

        System.out.println("JSON marshall / unmarshall: " + Long.toString(endTime - startTime) + " ms");
        System.out.println("JSON Size: " + Integer.toString(size));

        startTime = System.currentTimeMillis();
        for (i = 0; i < iterations; i++) {
            size = pbTest(customerPB);
        }
        endTime = System.currentTimeMillis();

        System.out.println("ProtoBuf marshall / unmarshall: " + Long.toString(endTime - startTime) + " ms");
        System.out.println("ProtoBuf Size: " + Integer.toString(size));
    }

    private static int xmlTest(Customer customer) {
        try {
            JAXBContext context = JAXBContext.newInstance(Customer.class);
            Marshaller marshaller = context.createMarshaller();

            ByteArrayOutputStream out = new ByteArrayOutputStream();

            marshaller.marshal(customer, out);

            byte[] data = out.toByteArray();

            InputStream in = new ByteArrayInputStream(data);

            Unmarshaller unmarshaller = context.createUnmarshaller();

            unmarshaller.unmarshal(in);

            return data.length;

        } catch (JAXBException e) {
            e.printStackTrace();
        }

        return 0;
    }

    private static int jsonTest(Customer customer) {
        try {
            ObjectMapper mapper = new ObjectMapper();
            ByteArrayOutputStream out = new ByteArrayOutputStream();
            mapper.writeValue(out, customer);

            byte[] data = out.toByteArray();

            InputStream in = new ByteArrayInputStream(data);

            mapper.readValue(in, Customer.class);

            return data.length;
        } catch (Exception e) {
            e.printStackTrace();
        }

        return 0;
    }

    private static int pbTest(CustomerProtoBuf.CustomerPB customer) {
        try {
            ByteArrayOutputStream out = new ByteArrayOutputStream();

            customer.writeTo(out);

            byte[] data = out.toByteArray();

            InputStream in = new ByteArrayInputStream(data);

            CustomerProtoBuf.CustomerPB.parseFrom(in);

            return data.length;
        } catch (Exception e) {
            e.printStackTrace();
        }

        return 0;
    }
}
