rule auto_rule_20250727033050_9541 {
  strings:
    $o0 = "dword_412234" wide ascii nocase
    $o1 = "main_loop_entrance_0" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
    $o3 = "x402C44" wide ascii nocase
  condition:
    4 of ($o*)
}