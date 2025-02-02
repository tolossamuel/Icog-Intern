 ; merge past and recent bin
 ; stractuer of the bin
 ; (index((count $cnt_val) (index $idx_val) (_size $size_val)))
! (bind! &past-space (new-space))
! (bind! &recent-space (new-space))
! (add-atom &past-space (1 ( (count 1) (index 1) (size 1))))
! (add-atom &past-space (2 ( (count 10) (index 2) (size 1))))
! (add-atom &past-space (3 ( (count 1) (index 3) (size 1))))
! (add-atom &past-space (4 ( (count 5) (index 4) (size 1))))
! (add-atom &recent-space (4 ( (count 1) (index 4) (size 1))))
! (add-atom &recent-space (5 ( (count 1) (index 5) (size 1))))
! (add-atom &recent-space (3 ( (count 3) (index 3) (size 1))))
! (add-atom &recent-space (2 ( (count 5) (index 2) (size 1))))
 ; Function: calculateBiasWithCount
 ; ---------------------------------
 ; This function calculates a weighted count based on a bias factor.
 ; It checks if a past count exists for the given index in &past-space.
 ; If a match is found, it applies the formula:
 ;   updated_count = (bias * past_count) + ((1 - bias) * count_val)
 ; Otherwise, it returns count_val as is.
 ;
 ; Parameters:
 ;   - $count_val: The current count value.
 ;   - $index: The index to search for in &past-space.
 ;   - $bias: The weight factor for adjusting the count.
 ;
 ; Returns:
 ;   - The adjusted count if a past count is found, otherwise count_val.
(: calculateBiasWithCount (-> Number Number Number Number))

(= (calculateBiasWithCount $count_val $index $bias)

    (if (not ( == ( collapse (match &past-space ($index ( (count $past_count) (index $idx_val) (size $size_val))) ($past_count))) ()))
        (let* (

                ($past_val (match &past-space ($index ( (count $past_count) (index $idx_val) (size $size_val))) $past_count))    )
            (+ ( * $bias $past_val) ( * ( - 1 $bias) $count_val))
        )

    $count_val

))
 ; Function: merge_bin
 ; -------------------
 ; This function merges bins from &recent-space by adjusting their counts
 ; using a bias factor. It processes each bin, calculates a weighted count
 ; using calculateBiasWithCount, and updates &recent-space accordingly.
 ;
 ; Parameters:
 ;   - $bias: The weight factor used to adjust the count value.
 ;
 ; Process:
 ;   1. Iterates through &recent-space to retrieve bins.
 ;   2. Extracts count, index, and size values.
 ;   3. Computes a new count using calculateBiasWithCount.
 ;   4. Removes the old bin entry and adds the updated one.
 ;
 ; Returns:
 ;   - A confirmation message ("Merge bin completed").
(: merge_bin (-> Number empty))
(= (merge_bin $bias)
    (match &recent-space ($index ( (count $count_val) (index $idx_val) (size $size_val)))
        (let* (
                ($count_map ( cdr-atom (count $count_val)))
                ($count_val (car-atom $count_map))
                ($index_val $index)

                ($count_value (calculateBiasWithCount $count_val $index_val $bias))
                ($_ (remove-atom &recent-space ($index ( (count $count_val) (index $idx_val) (size $size_val)))))
                ($_ (add-atom &recent-space ($index ( (count $count_value) (index $idx_val) (size $size_val)))))

            )

        ("Merge bin completed")

    )))
! (merge_bin 0.5)
! (get-atoms &recent-space)
