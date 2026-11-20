"""Все тексты сайта. Для каждого ключа пара: (английский, русский)."""

T = {
    # меню и общее
    "nav_intro": ("Introduction", "Введение"),
    "nav_main": ("Analysis", "Основа"),
    "nav_concl": ("Conclusion", "Заключение"),
    "author": (
        "Author: Tajigul Diar,Yeslyamova Aidana Narxoz University",
        "Автор: Тажигул Диар, Нархоз,Еслямова Айдана ",
    ),

    # введение
    "i_title": ("Which jobs could automation replace", "Какие профессии может заменить автоматизация"),
    "i_caption": ("Probability theory project", "Проект по теории вероятностей"),
    "i_p1": (
        "In 2013, Oxford researchers Carl Frey and Michael Osborne estimated how susceptible 702 US "
        "occupations are to automation. For each occupation they gave a number from 0 to 1: the "
        "probability that it could be fully automated within the next decade or two. The work was "
        "published in 2017 in Technological Forecasting and Social Change.",
        "В 2013 году исследователи из Оксфорда Карл Фрей и Майкл Осборн оценили, насколько "
        "702 профессии США поддаются автоматизации. Для каждой профессии они назвали число "
        "от 0 до 1: вероятность того, что её можно полностью автоматизировать в ближайшие "
        "десять-двадцать лет. Работа вышла в 2017 году в журнале Technological Forecasting "
        "and Social Change.",
    ),
    "i_p2": (
        "We took a sample of 150 occupations from this list. For 40 of them there is data from the US "
        "Bureau of Labor Statistics (BLS): projected employment growth from 2025 to 2035 and the "
        "median wage in 2025.",
        "Мы взяли выборку из 150 профессий этого списка. Для 40 из них есть данные Бюро "
        "статистики труда США (BLS): прогноз роста занятости с 2025 по 2035 год и медианная "
        "зарплата за 2025 год. Названия профессий и групп оставлены на английском, как в источнике.",
    ),
    "i_q_h": ("What we want to find out", "Что мы хотим выяснить"),
    "i_q": (
        "- what share of occupations falls into the high-risk zone;\n"
        "- how the probabilities are distributed and whether a known distribution fits them;\n"
        "- how precisely the mean can be estimated from a sample of 150 occupations;\n"
        "- whether automation risk is related to wages and to growth in demand for the occupation.",
        "- какая часть профессий попадает в зону высокого риска;\n"
        "- как распределены вероятности и подходит ли для них какое-нибудь известное распределение;\n"
        "- насколько точно по выборке из 150 профессий оценивается среднее;\n"
        "- связан ли риск автоматизации с зарплатой и ростом спроса на профессию.",
    ),
    "i_read_h": ("How to read the probability", "Как читать вероятность"),
    "i_read": (
        "The closer the number is to 1, the easier it is to hand the work to an algorithm or a "
        "machine. It is an estimate of technical feasibility and does not forecast job losses. "
        "More on this in the conclusion.",
        "Чем ближе число к 1, тем легче работу передать алгоритму или машине. Это оценка "
        "технической возможности, прогнозом потери рабочих мест она не является. Подробнее "
        "об этом в заключении.",
    ),
    "i_m1": ("Occupations in the sample", "Профессий в выборке"),
    "i_m2": ("Mean probability", "Средняя вероятность"),
    "i_m3": ("High risk (p > 0.7)", "Высокий риск (p > 0.7)"),
    "i_look_h": ("Look up an occupation", "Посмотреть профессию"),
    "i_select": ("Occupation", "Профессия"),
    "i_look": (
        "Probability of automation {p:.3f}. Group: {group}. This is higher than for {below:.0%} of "
        "the occupations in the sample.",
        "Вероятность автоматизации {p:.3f}. Группа: {group}. Это выше, чем у {below:.0%} "
        "профессий выборки.",
    ),
    "i_look_extra": (
        "Projected employment growth from 2025 to 2035: {growth:.1f}%. Median wage in 2025: {wage} USD.",
        "Прогноз роста занятости с 2025 по 2035 год: {growth:.1f}%. Медианная зарплата в 2025 году: {wage} USD.",
    ),
    "i_expander": ("Full sample", "Вся выборка"),
    "i_cols": (["Occupation", "Group", "Probability"], ["Профессия", "Группа", "Вероятность"]),

    # основа
    "a_title": ("Analysis: data and calculations", "Основа: данные и расчёты"),
    "a_conv": (
        "Convention for the whole page: we read the number p of each occupation as the probability "
        "that the occupation turns out to be automatable. Strictly speaking it is an estimate from the "
        "Frey and Osborne model, but without this reading there is nothing to apply probability "
        "theory to.",
        "Договорённость на всю страницу: число p у каждой профессии мы читаем как вероятность "
        "того, что профессия окажется автоматизируемой. Строго говоря, это оценка модели Фрея и "
        "Осборна, но без такой трактовки теорию вероятностей применить не к чему.",
    ),
    "a_h1": ("1. Descriptive statistics", "1. Описательная статистика"),
    "a_stat_cols": (["Measure", "Value"], ["Показатель", "Значение"]),
    "a_stat_names": (
        ["Observations", "Mean", "Median", "Standard deviation", "Minimum", "First quartile",
         "Third quartile", "Maximum", "Skewness"],
        ["Число наблюдений", "Среднее", "Медиана", "Стандартное отклонение", "Минимум",
         "Первый квартиль", "Третий квартиль", "Максимум", "Асимметрия"],
    ),
    "a_s1": (
        "The mean is {mean:.2f} and the median is {median:.2f}. The median is larger because many "
        "values pile up near 1. A standard deviation of {std:.2f} is large for a variable on the "
        "interval from 0 to 1: its ceiling is about 0.5.",
        "Среднее {mean:.2f}, медиана {median:.2f}. Медиана больше, потому что много "
        "значений скопилось у единицы. Стандартное отклонение {std:.2f} велико для величины "
        "на отрезке от 0 до 1: потолок у него около 0.5.",
    ),
    "a_hist": (
        "The histogram looks like the letter U. The first bar has {first} occupations, the last has "
        "{last}, and each of the five bars between 0.2 and 0.7 has at most {mid}. The occupations "
        "split into two parts: some are almost certainly automatable, the others almost certainly are not.",
        "Гистограмма похожа на букву U. В первом столбце {first} профессий, в последнем "
        "{last}, а в каждом из пяти столбцов между 0.2 и 0.7 не больше {mid}. "
        "Профессии делятся на две части: одни почти наверняка поддаются автоматизации, другие почти "
        "наверняка нет.",
    ),
    "a_shapiro": (
        "The Shapiro-Wilk test rejects normality (p {p}), so these data need a model defined on the "
        "interval from 0 to 1.",
        "Критерий Шапиро-Уилка отвергает нормальность (p {p}), так что для этих "
        "данных нужна модель, заданная на отрезке от 0 до 1.",
    ),
    "a_h2": ("2. Fitting a distribution", "2. Подбор распределения"),
    "a_s2": (
        "A natural choice for a variable on the interval from 0 to 1 is the beta distribution. When "
        "both of its parameters are below 1, the density curves upward at both edges, which gives "
        "exactly this U shape.",
        "Для величины на отрезке от 0 до 1 естественно взять бета-распределение. Если оба его "
        "параметра меньше единицы, плотность загибается вверх у обоих краёв, то есть получается "
        "именно U-образная форма.",
    ),
    "a_params": (
        "The parameters were found by maximum likelihood: a = {a:.3f}, b = {b:.3f}. Both are below 1.",
        "Параметры найдены методом максимального правдоподобия: a = {a:.3f}, b = {b:.3f}. "
        "Оба меньше единицы.",
    ),
    "a_ks": (
        "The Kolmogorov-Smirnov test gives D = {d:.3f}, p {p}. That is almost exactly at the 0.05 "
        "level. The parameters were estimated from the same data, so the true p-value is somewhat "
        "lower. The beta model captures the shape only approximately and cannot be accepted without "
        "reservations.",
        "Критерий Колмогорова-Смирнова даёт D = {d:.3f}, p {p}. Это почти ровно на "
        "уровне 0.05. Параметры оценены по тем же данным, поэтому настоящий p-value немного ниже. "
        "Бета-модель передаёт форму данных приблизительно, и принимать её без оговорок нельзя.",
    ),
    "a_uniform": (
        "The uniform distribution, where all values are equally likely, is rejected much more firmly "
        "(chi-square test on five intervals, p {p}).",
        "Равномерное распределение, при котором все значения одинаково вероятны, отвергается "
        "гораздо увереннее (хи-квадрат по пяти интервалам, p {p}).",
    ),
    "a_h3": ("3. Proportions and the binomial model", "3. Доли и биномиальная модель"),
    "a_s3": (
        "Call an occupation high-risk (event H) if p > 0.7 and low-risk if p < 0.3. The rest are "
        "medium. If we pick an occupation at random, the probability of H is estimated by the "
        "proportion P(H) = {k}/{n} = {ph:.3f}.",
        "Назовём профессию высокорисковой (событие H), если p > 0.7, и низкорисковой, если "
        "p < 0.3. Остальные средние. Если выбрать профессию наугад, вероятность H оценивается "
        "долей: P(H) = {k}/{n} = {ph:.3f}.",
    ),
    "a_cat_col": ("Category", "Категория"),
    "a_cat_cols": (["Count", "Share", "95% Wilson interval"], ["Число", "Доля", "95% интервал Уилсона"]),
    "a_cat_names": (
        ["Low (p < 0.3)", "Medium", "High (p > 0.7)"],
        ["Низкий (p < 0.3)", "Средний", "Высокий (p > 0.7)"],
    ),
    "a_range": ("{lo:.3f} to {hi:.3f}", "от {lo:.3f} до {hi:.3f}"),
    "a_wilson": (
        "For high risk the interval is from {lo:.3f} to {hi:.3f}. If we repeated the sampling many "
        "times, an interval built this way would cover the true proportion in about 95% of cases.",
        "Для высокого риска интервал от {lo:.3f} до {hi:.3f}. Это значит, что при "
        "повторных выборках такой интервал накрывает настоящую долю примерно в 95% случаев.",
    ),
    "a_binom": (
        "Now pick n occupations at random. The number of high-risk ones among them, X, follows a "
        "binomial distribution with p = {ph:.3f}.",
        "Теперь возьмём наугад n профессий. Число высокорисковых среди них, X, подчиняется "
        "биномиальному закону с p = {ph:.3f}.",
    ),
    "a_slider_n": ("How many occupations we pick (n)", "Сколько профессий выбираем (n)"),
    "a_slider_k": ("At least k high-risk occupations", "Нужно не меньше k высокорисковых"),
    "a_binom_res": (
        "P(X ≥ {k}) = {pb:.4f} under the binomial model and {pf:.4f} under the exact hypergeometric "
        "model, where sampling is without replacement. The expected number of high-risk occupations "
        "is {mean:.2f}, the standard deviation is {sd:.2f}.",
        "P(X ≥ {k}) = {pb:.4f} по биномиальной модели и {pf:.4f} по точной "
        "гипергеометрической, где выбор идёт без возвращения. Ожидаемое число высокорисковых "
        "профессий {mean:.2f}, стандартное отклонение {sd:.2f}.",
    ),
    "a_binom_cap": ("Bars where X ≥ k are dark.", "Тёмным показаны столбцы, где X ≥ k."),
    "a_h4": ("4. Mean and confidence interval", "4. Среднее и доверительный интервал"),
    "a_s4a": (
        "The sample mean is {m:.3f} and the standard error is {se:.3f}. The 95% confidence interval "
        "is built like this:",
        "Выборочное среднее {m:.3f}, стандартная ошибка {se:.3f}. Доверительный интервал 95% "
        "строится так:",
    ),
    "a_s4b": ("This gives {lo:.3f} to {hi:.3f}.", "Получаем от {lo:.3f} до {hi:.3f}."),
    "a_s4c": (
        "The data are not normal, but n = {n}, so by the central limit theorem the mean is "
        "approximately normal. As a check we ran a bootstrap: 10,000 times we drew a sample of 150 "
        "values with replacement and computed the mean. The bootstrap interval is from {lo:.3f} to "
        "{hi:.3f}, almost the same as the first.",
        "Данные не нормальные, зато n = {n}, и по центральной предельной теореме среднее "
        "приблизительно нормально. Для проверки мы сделали бутстреп: 10 000 раз взяли выборку "
        "из 150 значений с возвращением и посчитали среднее. Интервал по бутстрепу от {lo:.3f} "
        "до {hi:.3f}, он почти совпал с первым.",
    ),
    "a_s4d": (
        "The original data are U-shaped, yet the sample means form a bell, as the central limit "
        "theorem promises.",
        "Исходные данные U-образные, а средние выборок образуют колокол, как и обещает "
        "центральная предельная теорема.",
    ),
    "a_h5": ("5. Conditional probability and Bayes' formula", "5. Условная вероятность и формула Байеса"),
    "a_s5": (
        "Let G denote the event \"the occupation belongs to a given group\". The share of high-risk "
        "occupations within the group is P(H | G). The reverse quantity P(G | H) shows what part of "
        "all high-risk occupations falls into the group. Bayes' formula links the two:",
        "Пусть G обозначает событие «профессия из данной группы». Доля высокорисковых внутри группы "
        "равна P(H | G). Обратная величина P(G | H) показывает, какая часть всех высокорисковых "
        "профессий приходится на группу. Между ними связь по формуле Байеса:",
    ),
    "a_s5ex": (
        "Example: the group {g}. It has {n} of the {N} occupations in the sample, so P(G) = {pg:.3f}. "
        "Within the group P(H | G) = {phg:.3f}. Then P(G | H) = {phg:.3f} · {pg:.3f} / {ph:.3f} = "
        "{pgh:.3f}. So {pgh:.0%} of all high-risk occupations belong to this group, although the "
        "group makes up {pg:.0%} of the sample.",
        "Пример: группа {g}. В выборке в ней {n} профессий из {N}, поэтому P(G) = {pg:.3f}. "
        "Внутри группы P(H | G) = {phg:.3f}. Тогда P(G | H) = {phg:.3f} · {pg:.3f} / {ph:.3f} = "
        "{pgh:.3f}. Выходит, что {pgh:.0%} всех высокорисковых профессий относятся к этой "
        "группе, хотя сама группа занимает {pg:.0%} выборки.",
    ),
    "a_s5cap": (
        "Groups with at least 5 occupations are shown. For smaller groups the share is too unstable.",
        "В график попали группы, где не меньше 5 профессий. Для групп поменьше доля слишком неустойчива.",
    ),
    "a_s5cols": (
        ["Group", "Occupations", "Of them high-risk", "Mean p", "P(H | G)", "P(G | H)"],
        ["Группа", "Профессий", "Из них высокого риска", "Средняя p", "P(H | G)", "P(G | H)"],
    ),
    "a_kw": (
        "To check whether p depends on the group we applied the Kruskal-Wallis test to the {g} groups "
        "with at least 5 occupations: H = {h:.1f}, p {p}. So the probability clearly depends on the group.",
        "Чтобы проверить, зависит ли p от группы, мы применили критерий Краскела-Уоллиса к "
        "{g} группам с числом профессий не меньше 5: H = {h:.1f}, p {p}. "
        "Значит, вероятность заметно зависит от группы.",
    ),
    "a_h6": (
        "6. How many of the 150 occupations get automated",
        "6. Сколько профессий из 150 автоматизируется",
    ),
    "a_s6a": (
        "Let X_i be 1 if occupation i is automated and 0 otherwise, with P(X_i = 1) = p_i. If the "
        "occupations are independent, the number of automated ones is N = X_1 + … + X_150. Its mean "
        "and variance are simple sums:",
        "Пусть X_i равно 1, если профессия i автоматизирована, и 0 иначе, причём P(X_i = 1) = p_i. "
        "Если профессии независимы, число автоматизированных N = X_1 + … + X_150. Среднее и "
        "дисперсия считаются простой суммой:",
    ),
    "a_s6b": (
        "E[N] = {e:.1f}, standard deviation {sd:.2f}. The Monte Carlo method (20,000 runs) gives a "
        "mean of {m:.1f} and a 95% range from {lo:.0f} to {hi:.0f} occupations.",
        "E[N] = {e:.1f}, стандартное отклонение {sd:.2f}. Метод Монте-Карло (20 000 прогонов) "
        "даёт среднее {m:.1f} и 95% промежуток от {lo:.0f} до {hi:.0f} профессий.",
    ),
    "a_s6c": (
        "The expected share of {e:.0%} is higher than the share of high-risk occupations ({ph:.0%}), "
        "because occupations with medium probability also add to the sum. Independence does not hold "
        "in practice: occupations within one group tend to be automated together, so the real spread "
        "is wider than the simulation shows.",
        "Ожидаемая доля {e:.0%} выше доли высокорисковых профессий ({ph:.0%}), потому что "
        "профессии со средней вероятностью тоже вносят свой вклад в сумму. Независимость на практике "
        "не выполняется: профессии внутри одной группы автоматизируются вместе, поэтому реальный "
        "разброс шире, чем показывает симуляция.",
    ),
    "a_h7": ("7. Risk, wages and employment growth", "7. Риск, зарплата и рост занятости"),
    "a_s7a": (
        "Only {n} occupations have BLS data. We measure the relationship with the Pearson correlation "
        "coefficient and, since the distribution of p is not normal, also with the Spearman coefficient.",
        "Здесь только {n} профессий, для которых есть данные BLS. Взаимосвязь измеряем "
        "коэффициентом корреляции Пирсона, а так как распределение p не нормальное, ещё и "
        "коэффициентом Спирмена.",
    ),
    "a_corr_cols": (
        ["Pearson r", "p for r", "Spearman ρ", "p for ρ"],
        ["Пирсон r", "p для r", "Спирмен ρ", "p для ρ"],
    ),
    "a_corr_rows": (
        ["Probability and wage", "Probability and employment growth"],
        ["Вероятность и зарплата", "Вероятность и рост занятости"],
    ),
    "a_reg": (
        "Regression line for wages: {a} - {b} · p. A rise of 0.1 in p goes with a drop in the median "
        "wage of about {d} USD.",
        "Линия регрессии для зарплаты: {a} - {b} · p. Рост p на 0.1 связан со снижением "
        "медианной зарплаты примерно на {d} USD.",
    ),
    "a_cmp": (
        "Another comparison: the median wage in high-risk occupations is {hi} USD ({nh} of them), in "
        "low-risk ones {lo} USD ({nl} of them). The Mann-Whitney test gives p {p}. There are few "
        "high-risk occupations, so the conclusion is cautious.",
        "Ещё одно сравнение: медианная зарплата в высокорисковых профессиях {hi} USD "
        "(их {nh}), в низкорисковых {lo} USD (их {nl}). Критерий "
        "Манна-Уитни дал p {p}. Высокорисковых профессий мало, поэтому вывод осторожный.",
    ),
    "a_weight": (
        "If we weight p by employment in 2025, the mean over these {n} occupations is {w:.2f}, against "
        "{m:.2f} without weights. The reason is that high-risk occupations account for {es:.0%} of "
        "employment, while they are only {ps:.0%} of the occupations in this set.",
        "Если взвесить p по числу занятых в 2025 году, среднее по этим {n} профессиям "
        "равно {w:.2f}, без весов {m:.2f}. Причина в том, что на "
        "высокорисковые профессии приходится {es:.0%} занятых, а самих "
        "профессий среди сорока только {ps:.0%}.",
    ),
    "a_bias": (
        "BLS publishes only the fastest-growing occupations and those adding the most jobs. The link "
        "with employment growth comes from such a biased sample, and correlation alone does not show "
        "a cause.",
        "BLS публикует только самые быстрорастущие профессии и профессии с самым большим приростом "
        "рабочих мест. Связь с ростом занятости получена на такой смещённой выборке, а корреляция "
        "сама по себе причину не показывает.",
    ),

    # заключение
    "c_title": ("Conclusion", "Заключение"),
    "c_h1": ("What we found", "Что получилось"),
    "c1": (
        "The mean probability of automation in the sample is {m:.2f}, with a 95% confidence interval "
        "from {lo:.2f} to {hi:.2f}. {k} of {n} occupations, or {share:.0%}, are above 0.7.",
        "Средняя вероятность автоматизации по выборке {m:.2f}, 95% доверительный интервал от "
        "{lo:.2f} до {hi:.2f}. Выше 0.7 лежат {k} профессий из {n}, то есть {share:.0%}.",
    ),
    "c2": (
        "The distribution of probabilities is U-shaped: occupations cluster near 0 and near 1, and the "
        "middle is almost empty. A beta distribution with parameters {a:.2f} and {b:.2f} resembles the "
        "data, but the Kolmogorov-Smirnov test gives p {p}, which is the edge of significance.",
        "Распределение вероятностей U-образное: профессии сгруппированы у нуля и у единицы, "
        "середина почти пуста. Бета-распределение с параметрами {a:.2f} и {b:.2f} похоже на "
        "данные, но критерий Колмогорова-Смирнова даёт p {p}, это граница значимости.",
    ),
    "c3": (
        "Risk depends strongly on the group. In {g}, {share:.0%} of occupations are high-risk. In "
        "{zero} there are none in the sample.",
        "Риск сильно зависит от группы. В группе {g} высокорисковых профессий "
        "{share:.0%}. В группах {zero} их в выборке нет совсем.",
    ),
    "c4": (
        "If the occupations are treated as independent, about {e:.0f} of the {n} get automated on "
        "average, with a deviation of about {sd:.0f}.",
        "Если считать профессии независимыми, из {n} автоматизируется в среднем {e:.0f}, "
        "с отклонением около {sd:.0f}.",
    ),
    "c5": (
        "Among the {n} occupations with BLS data, risk is related to wages (r = {rw:.2f}) and to "
        "employment growth (r = {rg:.2f}). The higher the probability of automation, the lower both "
        "tend to be.",
        "Среди {n} профессий с данными BLS риск связан с зарплатой (r = "
        "{rw:.2f}) и с ростом занятости (r = {rg:.2f}). "
        "Чем выше вероятность автоматизации, тем ниже в среднем и то, и другое.",
    ),
    "c_h2": ("Limitations", "Ограничения"),
    "c_lim": (
        "- The probabilities were estimated in 2013, before modern language models. They show the "
        "technical feasibility of full automation, not a forecast of job losses.\n"
        "- The sample is not fully random. 40 occupations were included because BLS has data for them, "
        "and the other 110 were drawn at random from the remaining 662, with the category shares "
        "matched to the full list of 702.\n"
        "- The calculations in section 6 assume that occupations are independent. This is a "
        "simplification, and the real spread is larger.\n"
        "- The BLS data cover the fastest-growing occupations, so conclusions about employment growth "
        "cannot be extended to the whole economy.\n"
        "- All data are for the US.",
        "- Вероятности оценены в 2013 году, до появления современных языковых моделей. Они "
        "показывают техническую возможность полной автоматизации, а не прогноз потери рабочих мест.\n"
        "- Выборка не полностью случайная. 40 профессий взяты потому, что для них есть данные BLS, "
        "остальные 110 выбраны случайно из оставшихся 662, и доли категорий подогнаны под полный "
        "список из 702.\n"
        "- Расчёты в разделе 6 предполагают независимость профессий. Это упрощение, реальный разброс "
        "больше.\n"
        "- Данные BLS относятся к самым быстрорастущим профессиям, поэтому выводы о росте занятости "
        "нельзя переносить на всю экономику.\n"
        "- Все данные по США.",
    ),
    "c_h3": ("Sources", "Источники"),
    "c_src": (
        "- Frey C. B., Osborne M. A. (2017). The Future of Employment: How susceptible are jobs to "
        "computerisation? Technological Forecasting and Social Change, 114, 254-280. "
        "[PDF](https://www.oxfordmartin.ox.ac.uk/downloads/academic/The_Future_of_Employment.pdf)\n"
        "- U.S. Bureau of Labor Statistics, Employment Projections 2025-35, table 1.3: "
        "[fastest-growing occupations](https://www.bls.gov/emp/tables/fastest-growing-occupations.htm)\n"
        "- U.S. Bureau of Labor Statistics, Employment Projections 2025-35, table 1.4: "
        "[occupations with the most job growth](https://www.bls.gov/emp/tables/occupations-most-job-growth.htm)",
        "- Frey C. B., Osborne M. A. (2017). The Future of Employment: How susceptible are jobs to "
        "computerisation? Technological Forecasting and Social Change, 114, 254-280. "
        "[PDF](https://www.oxfordmartin.ox.ac.uk/downloads/academic/The_Future_of_Employment.pdf)\n"
        "- U.S. Bureau of Labor Statistics, Employment Projections 2025-35, таблица 1.3: "
        "[fastest-growing occupations](https://www.bls.gov/emp/tables/fastest-growing-occupations.htm)\n"
        "- U.S. Bureau of Labor Statistics, Employment Projections 2025-35, таблица 1.4: "
        "[occupations with the most job growth](https://www.bls.gov/emp/tables/occupations-most-job-growth.htm)",
    ),
}
