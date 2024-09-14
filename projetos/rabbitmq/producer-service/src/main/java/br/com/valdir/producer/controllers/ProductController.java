package br.com.valdir.producer.controllers;

import br.com.valdir.producer.services.ProductService;
import dtos.ProductDTO;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import dtos // Assumindo que ProductDTO está no pacote dtos

import static org.springframework.http.HttpStatus.CREATED;

@RestController
@RequiredArgsConstructor
@RequestMapping(value = "/products")
public class ProductController {

    private final ProductService service;

    @PostMapping
    public ResponseEntity<ProductDTO> produces(@RequestBody ProductDTO dto) {
        service.createProduct(dto);
        return ResponseEntity.status(CREATED).build();
    }
}
import dtos.ProductDTO; // Assumindo que ProductDTO está no pacote dtos