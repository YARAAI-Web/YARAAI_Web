rule auto_rule_20250726144411_2141 {
  strings:
    $o0 = "lprcSrc2" wide ascii nocase
    $o1 = "x7B63u" wide ascii nocase
    $o2 = "SemaphoreW" wide ascii nocase
    $o3 = "x178D" wide ascii nocase
    $o4 = "dword_432CBE" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726144415_3879 {
  strings:
    $o0 = "xF89C8533" wide ascii nocase
    $o1 = "x1648u" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726144419_0117 {
  condition:
    auto_rule_20250726144411_2141 or auto_rule_20250726144415_3879
}