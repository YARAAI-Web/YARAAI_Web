rule auto_rule_20250727014308_0471 {
  strings:
    $o0 = "x2AAF18B9" wide ascii nocase
    $o1 = "xFFFFDC0E" wide ascii nocase
    $o2 = "xFFFF4F2E" wide ascii nocase
    $o3 = "xFFFEAFB8" wide ascii nocase
    $o4 = "xFFFFFFF3" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727014309_1943 {
  strings:
    $o0 = "xFFFEDBFB" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727014313_9932 {
  condition:
    auto_rule_20250727014308_0471 or auto_rule_20250727014309_1943
}