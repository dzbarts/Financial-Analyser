html_strategies = """<p><strong><u>Правило всех стратегий</u></strong>: чем больше период, взятый для некоторой стратегии, тем меньше риск.</p>

<p><strong>1. SMA (Simple Moving Average)</strong> – простая скользящая средняя.<br>
Она максимально прозрачно обозначает основные тенденции,<br>
а также побочные ценовые изменения.</p>

<p><u>Стратегия</u>: если цена пересекает медленную скользящую сверху вниз, то стоит <mark style="background-color: #7a65ba">продавать</mark>.<br>
В обратном случае <mark style="background-color: #7a65ba">покупать</mark>.</p>

<br>
<p><strong>2. twoSMA</strong> – тоже простая скользящая средняя,<br>
однако вместо цены берется быстро скользящая средняя.<br>
Также обозначает основные тенденции и побочные ценовые изменения.<br>
Для быстрой скользящей берется значение до половины медленной.</p>

<p><u>Стратегия</u>: если цена пересекает медленную скользящую сверху вниз,<br>
то стоит <mark style="background-color: #7a65ba">продавать</mark>. В обратном случае <mark style="background-color: #7a65ba">покупать</mark>.</p>

<br>
<p><strong>3. EMA (Exponential Moving Average)</strong> – разновидность скользящей средней,<br>
рассчитываемая экспоненциально. В сравнении с простой,<br>
экспонента придает гораздо больше важности текущим значениям, чем старым.</p>

<p><u>Стратегия</u>: если цена пересекает медленную скользящую сверху вниз,<br>
то стоит <mark style="background-color: #7a65ba">продавать<.mark>. В обратном случае <mark style="background-color: #7a65ba">покупать</mark>.</p>

<br>
<p><strong>4. DEMA (Double exponential moving average)</strong> – дважды взятая EMA,<br>
является более продвинутой, чем традиционные скользящие средние.</p>

<p><u>Стратегия</u>: если цена пересекает медленную скользящую сверху вниз,<br>
то стоит <mark style="background-color: #7a65ba">продавать</mark>. В обратном случае <mark style="background-color: #7a65ba">покупать</mark>.</p>

<br>
<p><strong>5. TEMA (Triple exponential moving average)</strong> – трижды взятая EMA,<br>
реагирует быстрее, что делает её более востребованной у трейдеров.</p>

<p><u>Стратегия</u>: если цена пересекает медленную скользящую сверху вниз,<br>
то стоит <mark style="background-color: #7a65ba">продавать<.mark>. В обратном случае <mark style="background-color: #7a65ba">покупать</mark>.</p>

<br>
<p><strong>6. MACD (Moving average convergence/divergence)</strong> – схождение/расхождение скользящих средних.</p>

<p><u>Стратегия</u>: если гистограмма пересекает сигнальную линию сверху вниз,<br>
то стоит <mark style="background-color: #7a65ba">продавать</mark>. В обратном случае <mark style="background-color: #7a65ba">покупать</mark>.</p>

<br>
<p><strong>7. Индикатор волатильности CHV (Chaikin Volatility)</strong> – индикатор,<br>
с помощью которого определяют волатильность рынка.</p>

<p><u>Стратегия</u>: начало роста индикатора может свидетельствовать<br>
о <mark style="background-color: #7a65ba">формировании очередного максимума цены</mark>. В таком случае волатильность<br>
будет увеличиваться до тех пор, пока этот экстремум не будет установлен.<br>
Быстрое снижение кривой CHV говорит о <mark style="background-color: #7a65ba">замедлении текущей тенденции</mark>.<br>
Вероятно, в ближайшее время произойдет сильная коррекция или откат цены.</p>

<br>
<p><strong>8. RSI (Relative strength index)</strong> – индекс перекупленности/перепроданности.<br>
Осциллятор (специальный индикатор, который прогнозирует тенденции рынка или акций)<br>
рассчитывается на основании цен закрытия и показывает,<br>
кто в данный момент доминирует на рынке: быки (покупатели) или медведи (продавцы).</p>

<p><u>Стратегия</u>: индикатор возвращает значения от 0 до 100,<br>
считается, что значения ниже 30 говорят о <mark style="background-color: #7a65ba">недооценности рынка (нужно покупать)</mark>,<br>
а выше 70 – о <mark style="background-color: #7a65ba">перекупленности (нужно продавать)</mark>.</p>

<br>
<p><strong>9. Индикатор Bulls Power</strong> – простой и эффективный инструмент анализа,<br>
применение которого позволяет определять настроения покупателей («быков»)<br>
в обозначенный период времени.</p>

<p><u>Стратегия</u>: если столбцы гистограммы растут,<br>
но значения пока меньше 0, то стоит <mark style="background-color: #7a65ba">покупать</mark>;<br>
если столбцы гистограммы падают, но значения пока больше 0,<br>
то стоит <mark style="background-color: #7a65ba">продавать</mark>.</p>

<br>
<p><strong>10. Индикатор Bears Power</strong> – классический осциллятор,<br>
определяющий силу продавцов («медведей») рынка в выбранный временной период.</p>

<p><u>Стратегия</u>: если столбцы гистограммы растут,<br>
но значения пока меньше 0, то стоит <mark style="background-color: #7a65ba">покупать</mark>;<br>
если столбцы гистограммы падают, но значения пока больше 0,<br>
то стоит <mark style="background-color: #7a65ba">продавать</mark>.</p>

<br>
<p><strong>11. Индикатор ER (Elder Rays)</strong> – комплексный индикатор.<br>
Цена определяется в результате компромисса между покупателями и продавцами.</p>

<p><u>Стратегия</u>: если столбцы гистограммы растут,<br>
но значения пока меньше 0, то стоит <mark style="background-color: #7a65ba">покупать</mark>;<br>
если столбцы гистограммы падают, но значения пока больше 0,<br>
то стоит <mark style="background-color: #7a65ba">продавать</mark>.</p>

<p><strong>12. Индикатор MI (Mass Index)</strong> – технический индикатор,<br>
использование которого дает возможность спрогнозировать разворот тренда<br>
за cчет анализа динамики изменений диапазона цен.</p>

<p><u>Стратегия</u>: если кривая пересекает линию 27 снизу вверх,<br>
а потом линию 26,5 сверху вниз, то следует <mark style="background-color: #7a65ba">покупать</mark>.<br>
</p>"""

html_strategies_eng = """<p><strong><u>The rule of all strategies</u></strong>: the longer the period taken for a certain strategy, the lower the risk. </p>

<p><strong>1. SMA (Simple Moving Average)</strong> is a simple moving average.<br>
It indicates the main trends as transparently as possible, as<br>
well as side price changes. </p>

<p><u>Strategy</u>: if the price crosses the slow moving from top to bottom, then it is <mark style="background-color: #7a65ba">worth selling</mark>.<br>
In the opposite case, <mark style="background-color: #7a65ba">buy</mark>. </p>

<br>
<p><strong>2. twoSMA</strong> is also a simple moving average,<br>
but a fast moving average is taken instead of the price.<br>
It also indicates the main trends and side price changes.<br>
For a fast moving average, a value of up to half of the slow one is taken. </p>

<p><u>Strategy</u>: if the price crosses the slow moving from top to bottom,<br>
then it is <mark style="background-color: #7a65ba">worth selling</mark>. In the opposite case, <mark style="background-color: #7a65ba">buy</mark>. </p>

<br>
<p><strong>3. EMA (Exponential Moving Average)</strong> is a kind of moving average<br>
calculated exponentially. In comparison with the simple one, the<br>
exponent attaches much more importance to the current values than to the old ones. </p>

<p><u>Strategy</u>: if the price crosses the slow moving from top to bottom,<br>
then it is <mark style="background-color: #7a65ba">worth selling</mark>. In the opposite case, <mark style="background-color: #7a65ba">buy</mark>. </p>

<br>
<p><strong>4. DEMA (Double exponential moving average)</strong> – twice taken EMA,<br>
it is more advanced than traditional moving averages. </p>

<p><u>Strategy</u>: if the price crosses the slow moving from top to bottom,<br>
then it is <mark style="background-color: #7a65ba">worth selling</mark>. In the opposite case, <mark style="background-color: #7a65ba">buy</mark>. </p>

<br>
<p><strong>5. TEMA (Triple exponential moving average</strong> - the EMA taken three times<br>
reacts faster, which makes it more in demand among traders. </p>

<p><u>Strategy</u>: if the price crosses the slow moving from top to bottom,<br>
then it is <mark style="background-color: #7a65ba">worth selling</mark>. In the opposite case, <mark style="background-color: #7a65ba">buy</mark>. </p>

<br>
<p><strong>6. MACD (Moving average convergence/divergence)</strong> – convergence/divergence of moving averages. </p>

<p><u>Strategy</u>: if the histogram crosses the signal line from top to bottom,<br>
then it is <mark style="background-color: #7a65ba">worth selling</mark>. In the opposite case, <mark style="background-color: #7a65ba">buy</mark>. </p>

<br>
<p><strong>7. The volatility indicator CHV (Chaikin Volatility)</strong> is an indicator<br>
used to determine the volatility of the market. </p>

<p><u>Strategy</u>: the beginning of the growth of the indicator may indicate<br>
the <mark style="background-color: #7a65ba">formation of another price maximum</mark>. In this case, volatility<br>
will increase until this extreme is established.<br>
The rapid decline of the CHV curve indicates a <mark style="background-color: #7a65ba">slowdown in the current trend</mark>.<br>
There is likely to be a strong correction or pullback in the price in the near future. </p>

<br>
<p><strong>8. RSI (Relative strength index)</strong> – overbought/oversold index.<br>
An oscillator (a special indicator that predicts market or stock trends) is<br>
calculated based on closing prices and shows<br>
who is currently dominating the market: bulls (buyers) or bears (sellers). </p>

<p><u>Strategy</u>: the indicator returns values from 0 to 100, it<br>
is believed that values below 30 indicate that the <mark style="background-color: #7a65ba">market is undervalued (you need to buy)</mark> <br>
and above 70 - <mark style="background-color: #7a65ba">overbought (you need to sell)</mark>. </p>

<br>
<p><strong>9. Bulls Power indicator</strong> is a simple and effective analysis tool,<br>
the use of which allows you to determine the mood of buyers ("bulls")<br>
in a designated period of time. </p>

<p><u>Strategy</u>: if the histogram columns are growing,<br>
but the values are still less than 0, then it is <mark style="background-color: #7a65ba">worth buying</mark>;<br>
if the histogram columns are falling, but the values are still greater than 0,<br>
it's <mark style="background-color: #7a65ba">worth selling</mark>. </p>

<br>
<p><strong>10. The Bears Power indicator</strong> is a classic oscillator that<br>
determines the strength of sellers ("bears") of the market in the selected time period. </p>

<p><u>Strategy</u>: if the histogram columns are growing,<br>
but the values are still less than 0, then it is <mark style="background-color: #7a65ba">worth buying</mark>;<br>
if the histogram columns are falling, but the values are still greater than 0,<br>
it's <mark style="background-color: #7a65ba">worth selling</mark>. </p>

<br>
<p><strong>11. The ER (Elder Rays)</strong> indicator is a complex indicator.<br>
The price is determined as a result of a compromise between buyers and sellers. </p>

<p><u>Strategy</u>: if the histogram columns are growing,<br>
but the values are still less than 0, then it is <mark style="background-color: #7a65ba">worth buying</mark>;<br>
if the histogram columns are falling, but the values are still greater than 0,<br>
it's <mark style="background-color: #7a65ba">worth selling</mark>. </p>

<p><strong>12. The MI indicator (Mass Index)</strong> is a technical indicator, the<br>
use of which makes it possible to predict a trend reversal<br>
by analyzing the dynamics of changes in the price range. </p>

<br>
<p><u>Strategy</u>: if the curve crosses line 27 from bottom to top,<br>
and then the line 26.5 from top to bottom, then you should <mark style="background-color: #7a65ba">buy</mark>.</p>"""