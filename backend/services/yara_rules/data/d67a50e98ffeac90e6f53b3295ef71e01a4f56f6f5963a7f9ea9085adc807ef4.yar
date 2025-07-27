rule auto_rule_20250727044553_5139 {
  strings:
    $o0 = "dword_4941B8" wide ascii nocase
    $o1 = "x2D76DAD4" wide ascii nocase
  condition:
    all of them
}