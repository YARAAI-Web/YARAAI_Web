rule auto_rule_20250726082559_7905 {
  strings:
    $o0 = "x8A9C" wide ascii nocase
    $o1 = "dword_428ECD" wide ascii nocase
    $o2 = "off_428485" wide ascii nocase
    $o3 = "xF89C85B9" wide ascii nocase
    $o4 = "x3272F8u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726082602_7736 {
  strings:
    $o0 = "dword_428E95" wide ascii nocase
    $o1 = "dword_428E89" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726082606_4803 {
  condition:
    auto_rule_20250726082559_7905 or auto_rule_20250726082602_7736
}