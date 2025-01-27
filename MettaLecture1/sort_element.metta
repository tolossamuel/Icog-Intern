;; This function sorts an array (list) of elements in ascending order.
;; It uses a recursive approach to sort the list.
(: sort_element (-> List List))  ;; Declaring the type signature of the function `sort_element`, which takes a list and returns a sorted list.
;; Base case: if the list is empty (Nil), return an empty list.
(= (sort_element Nil) Nil)  
;; Base case: if the list contains only one element, it's already sorted, so return the list as is.
(= (sort_element (:: $x Nil)) (:: $x Nil))
;; Recursive case: if the list has more than one element, sort the list by comparing the first two elements.
(= (sort_element (:: $x (:: $y $xs)))
   (if (< $x $y)  ;; If the first element is smaller than the second one...
       (:: $x (sort_element (:: $y $xs)))  ;; Add $x to the sorted version of the rest of the list
       (:: $y (sort_element (:: $x $xs)))))  ;; Otherwise, add $y to the sorted version of the rest of the list
;; This function sorts the entire array by calling `sort_element` recursively on the array, 
;; reducing the number of elements to sort with each recursive call.
( = (sort_all $x $n)
    (if (> $n 0)  ;; If the number of iterations left is greater than 0...
        (sort_all (sort_element $x) (- $n 1))  ;; Call sort_element and reduce the iteration count
        $x  ;; Once no iterations are left, return the sorted list
    )
)
;; Example call to the `sort_all` function.
!(sort_all (:: 5 (:: 6 (:: 2 Nil))) 3)  ;; Sort the list `(:: 5 (:: 6 (:: 2 Nil)))` with 3 iterations.
