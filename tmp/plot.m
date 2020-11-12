x = dlmread('oakland-mi-subset.csv',',',1,0);

%
% Shiva's plot
%
% X axis is the rate of R straight tickets per overall straight ticket
% voter
%
% Y axis is the rate of R indiv trump vote per overall indiv ballots 
%

st_rate = x(:,2)./x(:,3);
figure(1)
plot(st_rate(:),x(:,4)./x(:,5)-st_rate(:),'.')

%
% alternate 1
% 
% X axis is overall rate of trump votes, any source
%
% Y axis is difference between rate of R straight ticket per overall
% straight tickets, and rate of trump votes per overall indiv ballots
%

r_rate = (x(:,2)+x(:,4))./(x(:,3)+x(:,5));
figure(2)
plot(r_rate(:),x(:,4)./x(:,5)-x(:,2)./x(:,3),'.')

%
% alternate 2
%
% X axis is overall rate of trump votes, any source 
%
% Y axis is difference between rate of individual trump votes per all votes, 
% and the rate of R straight ticket votes per all votes
%
% shows that as the overall fraction of trump votes increases, the fraction
% of stright ticket votes increases relative to individual, linearly.
%

figure(3)
plot(r_rate(:),x(:,2)./(x(:,3)+x(:,5))-x(:,4)./(x(:,3)+x(:,5)),'.')

%
% X = straight_r_votes / total_votes
%
% Y = (trump_votes_among_mixed_ballots / mixed_ballot_votes) - 
%    (trump_votes_among_straight_r_ballots / straight_r_votes)
%

figure(4)
str_per_total = x(:,2)./(x(:,3)+x(:,5));
plot(str_per_total(:),x(:,4)./x(:,5)-x(:,2)./x(:,3),'.')

