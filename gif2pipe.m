address = './pipe_as_gif/';
damage_type = {'dent','slit','impi','squiz','nd'};
label = [1,2,3,4,5];
damage_sample_size = 100;
L = 200;
resize = 0.5;
H = 640*resize;
W = 480*resize;

for t = 1:numel(label)
    X = zeros(L*damage_sample_size, H*W);
    for i = 1:damage_sample_size+1
        fprintf('%d',i);
        file = [address,damage_type{t},num2str(i),'.gif'];
        gif=imread(file,'frames','all');
        for ii= 1:L
            im=gif(:,:,:,ii);
            imm = imresize(im2bw(im),resize);
            X((i-1)*L + ii,:)=imm(:)';
        end
    end
    save_file = [address,damage_type{t},'.mat'];
    save(save_file,'X','-v7.3');
end