package com.cloudcomputing.deleteproducer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication(scanBasePackages = {"com.cloudcomputing.models","com.cloudcomputing.repositories","com.cloudcomputing.controllers"})
@EnableDiscoveryClient
@ComponentScan({"com.cloudcomputing.models","com.cloudcomputing.repositories","com.cloudcomputing.controllers"})
@EntityScan(basePackages={"com.cloudcomputing.models","com.cloudcomputing.repositories","com.cloudcomputing.controllers"})
@EnableJpaRepositories("com.cloudcomputing.repositories")
public class DeleteProducerApplication {

	public static void main(String[] args) {
		SpringApplication.run(DeleteProducerApplication.class, args);
	}

}
