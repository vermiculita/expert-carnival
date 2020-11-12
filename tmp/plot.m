x = dlmread('oakland-mi-subset.csv',',',1,0);
st_rate = x(:,2)./x(:,3);
figure(1)
plot(st_rate(:),x(:,4)./x(:,5)-st_rate(:),'.')

r_rate = (x(:,2)+x(:,4))./(x(:,3)+x(:,5));
figure(2)
plot(r_rate(:),x(:,4)./x(:,5)-x(:,2)./x(:,3),'.')