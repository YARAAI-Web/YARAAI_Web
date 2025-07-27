rule auto_rule_20250727023556_6637 {
  strings:
    $o0 = "x459974" wide ascii nocase
    $o1 = "__inbyte" wide ascii nocase
    $o2 = "byte_791318" wide ascii nocase
    $o3 = "x6FAFu" wide ascii nocase
    $o4 = "byte_7CFEA2" wide ascii nocase
  condition:
    4 of ($o*)
}