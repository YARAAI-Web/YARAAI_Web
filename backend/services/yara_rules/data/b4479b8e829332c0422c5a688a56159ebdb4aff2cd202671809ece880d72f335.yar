rule auto_rule_20250726085425_6302 {
  strings:
    $o0 = "word_45D030" wide ascii nocase
    $o1 = "__from_strstr_to_strchr" wide ascii nocase
  condition:
    all of them
}