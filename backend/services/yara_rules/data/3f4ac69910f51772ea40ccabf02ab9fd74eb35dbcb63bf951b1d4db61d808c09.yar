rule auto_rule_20250727014036_9697 {
  strings:
    $o0 = "__freetlocinfo" wide ascii nocase
    $o1 = "TrailDown0_0" wide ascii nocase
    $o2 = "RtlUnwind" wide ascii nocase
    $o3 = "__sbh_resize_block" wide ascii nocase
    $o4 = "dword_46EA78" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250727014039_5518 {
  strings:
    $o0 = "word_45458A" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727014050_7149 {
  condition:
    auto_rule_20250727014036_9697 or auto_rule_20250727014039_5518
}