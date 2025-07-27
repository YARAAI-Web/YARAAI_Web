rule auto_rule_20250726180503_2381 {
  strings:
    $o0 = "x8312297u" wide ascii nocase
    $o1 = "x49681C8Eu" wide ascii nocase
    $o2 = "x36A6546Au" wide ascii nocase
    $o3 = "fcmovu" wide ascii nocase
    $o4 = "fsubr" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726180507_0869 {
  strings:
    $o0 = "x39E122C2u" wide ascii nocase
    $o1 = "x18EE5DF9u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726180511_7454 {
  condition:
    auto_rule_20250726180503_2381 or auto_rule_20250726180507_0869
}