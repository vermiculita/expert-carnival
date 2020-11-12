x = dlmread('oakland-mi-subset.csv',',',1,0);
st_rate = x(:,2)./x(:,3);
plot(st_rate(:),x(:,4)./x(:,5)-st_rate(:),'.')