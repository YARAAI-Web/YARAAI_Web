rule auto_rule_20250726230348_4041 {
  strings:
    $o0 = "dword_45CEFC" wide ascii nocase
  condition:
    all of them
}