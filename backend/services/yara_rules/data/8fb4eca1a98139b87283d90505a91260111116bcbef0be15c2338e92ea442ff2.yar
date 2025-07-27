rule auto_rule_20250727042938_9126 {
  strings:
    $o0 = "byte_4845C4" wide ascii nocase
    $o1 = "_IsZeroMan" wide ascii nocase
    $o2 = "main_loop_entrance" wide ascii nocase
    $o3 = "_RoundMan" wide ascii nocase
  condition:
    4 of ($o*)
}