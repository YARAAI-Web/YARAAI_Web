rule auto_rule_20250726121325_1489 {
  strings:
    $o0 = "ReferencedDomainName" wide ascii nocase
    $o1 = "dword_42E899" wide ascii nocase
    $o2 = "dword_42E6D1" wide ascii nocase
    $o3 = "x481D00000503LL" wide ascii nocase
    $o4 = "x62FCu" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726121327_8361 {
  strings:
    $o0 = "x2B09u" wide ascii nocase
    $o1 = "x98787667" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726121332_4315 {
  condition:
    auto_rule_20250726121325_1489 or auto_rule_20250726121327_8361
}