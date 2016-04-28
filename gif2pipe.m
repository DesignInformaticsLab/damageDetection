function [pipe]=gif2pipe(gif)
% eg. gif=imread('dent1.gif','frames','all');

[a,b,~,d]=size(gif);

pipe=zeros(a,b,d);

for i=1:d
    im=gif(:,:,:,i);
    pipe(:,:,i)=im2bw(im);
end

end