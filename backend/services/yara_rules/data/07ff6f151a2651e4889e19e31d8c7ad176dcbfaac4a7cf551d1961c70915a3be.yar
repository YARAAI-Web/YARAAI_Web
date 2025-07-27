rule auto_rule_20250726124345_9227 {
  strings:
    $o0 = "dword_43B0B2" wide ascii nocase
    $o1 = "aFilitomo" wide ascii nocase
    $o2 = "dword_43B04C" wide ascii nocase
    $o3 = "dword_43B090" wide ascii nocase
    $o4 = "x54AFDE00" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726124347_6547 {
  strings:
    $o0 = "dword_43B670" wide ascii nocase
    $o1 = "x2940A200u" wide ascii nocase
    $o2 = "dword_43B3DC" wide ascii nocase
    $o3 = "dword_43B510" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726124350_2646 {
  condition:
    auto_rule_20250726124345_9227 or auto_rule_20250726124347_6547
}