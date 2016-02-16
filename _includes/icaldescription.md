{{ 'ABSTRACT:\n\n' |
   append: item_seminar.abstract | 
   append: '\n\n' |
   append: 'BIO:\n\n' | 
   append: item_seminar.bio | 
   newline_to_br | 
   strip_newlines | 
   replace: '<br /><br />','\n\n' | 
   replace: '<br />- ','\n- ' | 
   replace: '<br />* ','\n- ' | 
   remove: '<br />' }}
