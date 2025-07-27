rule auto_rule_20250726080317_5023 {
  strings:
    $o0 = "dword_404FB0" wide ascii nocase
    $o1 = "_vbaChkstk" wide ascii nocase
    $o2 = "word_409044" wide ascii nocase
    $o3 = "_vbaVargVar" wide ascii nocase
  condition:
    4 of ($o*)
}