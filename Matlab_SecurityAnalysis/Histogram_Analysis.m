% clc
% % Reading images
% encrypted_image = imread("512_CM_encrypted.png");
% plain_image = imread("512 x 512.png");
% % Split RGB components
% plain_R = plain_image(:,:,1);
% plain_G = plain_image(:,:,2);
% plain_B = plain_image(:,:,3);
% encrypted_R = encrypted_image(:,:,1);
% encrypted_G = encrypted_image(:,:,2);
% encrypted_B = encrypted_image(:,:,3);
% 
% % Histograms for R, G, B components of plain image
% subplot(2, 3, 1);
% imhist(plain_R);
% title('Plain Image R Histogram');
% subplot(2, 3, 2);
% imhist(plain_G);
% title('Plain Image G Histogram');
% subplot(2, 3, 3);
% imhist(plain_B);
% title('Plain Image B Histogram');
% 
% % Histograms for R, G, B components of encrypted image
% subplot(2, 3, 4);
% imhist(encrypted_R);
% title('Encrypted Image R Histogram');
% subplot(2, 3, 5);
% imhist(encrypted_G);
% title('Encrypted Image G Histogram');
% subplot(2, 3, 6);
% imhist(encrypted_B);
% title('Encrypted Image B Histogram');
 
clc;
% Read images
encrypted_image = imread("512_LM_encrypted.png");
plain_image = imread("512 x 512.png");

% Split RGB components
plain_R = plain_image(:,:,1);
plain_G = plain_image(:,:,2);
plain_B = plain_image(:,:,3);
encrypted_R = encrypted_image(:,:,1);
encrypted_G = encrypted_image(:,:,2);
encrypted_B = encrypted_image(:,:,3);

% Get histograms
[plain_hist_R, bins] = imhist(plain_R);
plain_hist_G = imhist(plain_G);
plain_hist_B = imhist(plain_B);

[enc_hist_R, ~] = imhist(encrypted_R);
enc_hist_G = imhist(encrypted_G);
enc_hist_B = imhist(encrypted_B);

% Plot combined histogram for plain image using bar (mimicking imhist)
subplot(1, 2, 1);
hold on;
bar(bins, plain_hist_R, 'r', 'FaceAlpha', 0.4, 'EdgeColor', 'r');
bar(bins, plain_hist_G, 'g', 'FaceAlpha', 0.4, 'EdgeColor', 'g');
bar(bins, plain_hist_B, 'b', 'FaceAlpha', 0.4, 'EdgeColor', 'b');
hold off;
title('c');
xlabel('Pixel Intensity');
ylabel('Frequency');
legend('Red', 'Green', 'Blue');
grid on;

% Plot combined histogram for encrypted image
subplot(1, 2, 2);
hold on;
bar(bins, enc_hist_R, 'r', 'FaceAlpha', 0.4, 'EdgeColor', 'r');
bar(bins, enc_hist_G, 'g', 'FaceAlpha', 0.4, 'EdgeColor', 'g');
bar(bins, enc_hist_B, 'b', 'FaceAlpha', 0.4, 'EdgeColor', 'b');
hold off;
title('f');
xlabel('Pixel Intensity');
ylabel('Frequency');
legend('Red', 'Green', 'Blue');
grid on;
