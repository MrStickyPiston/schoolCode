#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define KEY_SIZE 88


char* encrypt(char* message, char* key) {
    int message_length = strlen(message);
    char* encrypted_message = malloc((message_length + 1) * sizeof(char));
    for (int i = 0; i < message_length; i++) {
        encrypted_message[i] = message[i] ^ key[i % KEY_SIZE];
    }
    encrypted_message[message_length] = '\0';
    return encrypted_message;
}

char* decrypt(char* encrypted_message, char* key) {
    int message_length = strlen(encrypted_message);
    char* decrypted_message = malloc((message_length + 1) * sizeof(char));
    for (int i = 0; i < message_length; i++) {
        decrypted_message[i] = encrypted_message[i] ^ key[i % KEY_SIZE];
    }
    decrypted_message[message_length] = '\0';
    return decrypted_message;
}

int main() {
    char* key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;':\",.<>/?`~";
    char* encrypted_message = encrypt("StickyPiston on top", key);
    printf("Encrypted message: %s\n", encrypted_message);
    char* decrypted_message = decrypt(encrypted_message, key);
    printf("Decrypted message: %s\n", decrypted_message);
    return 0;
}
