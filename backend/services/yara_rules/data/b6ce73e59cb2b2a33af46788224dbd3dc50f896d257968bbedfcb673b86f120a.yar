rule auto_rule_20250727015550_7669 {
  strings:
    $o0 = "__outdword" wide ascii nocase
    $o1 = "__readgsqword" wide ascii nocase
    $o2 = "xmmword_1C688" wide ascii nocase
    $o3 = "x1BD07" wide ascii nocase
    $o4 = "xmmword_1C698" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727015553_2161 {
  strings:
    $o0 = "x214BDBF" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727015557_9446 {
  condition:
    auto_rule_20250727015550_7669 or auto_rule_20250727015553_2161
}